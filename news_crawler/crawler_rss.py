import feedparser, mysql.connector, threading, os
from time import mktime, localtime, strftime, sleep
from datetime import datetime

mysql_host = os.environ.get('MYSQL_HOST', 'localhost')
mysql_user = os.environ.get('MYSQL_USER', 'root')
mysql_password = os.environ.get('MYSQL_PASS', 'root')
mysql_database = os.environ.get('MYSQL_DATABASE', 'gpn')

blacklist = ('pequenas-empresas-grandes-negocios',
					'banco-do-brasil',
					'bb',
					'bradesco',
					'itau',
					'caixa-economica',
					'santander',
					'cef',
					'nubank',
					'lula',
					'dilma',
					'aecio',
					'bolsonaro',
					'ciro-gomes',
					'pt',
					'mdb',
					'psdb')

print('Iniciando Crawler...')
sleep(30)
while True:
	sleep(30)
	print(strftime("%Y-%m-%d %H:%M:%S", localtime()) + ' Atualizando G1...')
	d = feedparser.parse('http://pox.globo.com/rss/g1/economia/')
	registros = []
	for noticia in d['entries']:
		#noticia['published_parsed'] # Data hora da publicacao
		#noticia['summary_detail'] # Resumo detalhado da noticia
		#noticia['links'] # Link para a noticia
		#noticia['tags'] # Tags (so tem term: G1)
		#noticia['summary'] # Resumo da noticia
		#noticia['guidislink'] # Todos estao False
		#noticia['title_detail'] # Titulo detalhado da noticia
		#noticia['link'] # Link para a noticia
		#noticia['published'] # Data hora textual da publicacao
		link = noticia['link'][noticia['link'].find('://g1.globo.com/')+16:]
		if link[:link.find('/')] == 'economia':
			link = link[link.find('/')+1:]
			editoria = link[:link.find('/')].replace('-', ' ').upper()
			if editoria in ('BLOG'):
				continue
			elif editoria == 'NOTICIA':
				editoria = 'ECONOMIA'
			elif editoria == 'PME':
				editoria = 'PEQUENAS EMPRESAS GRANDES NEGÓCIOS'
			elif editoria == 'EDUCACAO FINANCEIRA':
				editoria = 'EDUCAÇÃO FINANCEIRA'
			elif editoria == 'AGRONEGOCIOS':
				editoria = 'AGRONEGÓCIOS'
			
			texto = link[link.rfind('/'):]
			if len(texto) < 10:
				continue

			incluir = True
			for palavra in blacklist:
				if palavra in texto:
					incluir = False

			if not incluir:
				continue

			registro = {}
			registro['id'] = noticia['id'] # Link para a noticia
			registro['fonte'] = 'G1'
			registro['editoria'] = editoria
			registro['titulo'] = noticia['title'] # Titulo da noticia
			registro['data_atualizacao'] = datetime.fromtimestamp(mktime(noticia['published_parsed'])).date()
			registro['hora_atualizacao'] = datetime.fromtimestamp(mktime(noticia['published_parsed'])).time()
			registros.append(registro)

	conexao = mysql.connector.connect(host=mysql_host, user=mysql_user, password=mysql_password, database=mysql_database)
	cursor = conexao.cursor()
	add_noticia = ("REPLACE INTO `noticias` (ID, FONTE, EDITORIA, TITULO, DATA_ATUALIZACAO, HORA_ATUALIZACAO) \
					VALUES (%(ID)s, %(FONTE)s, %(EDITORIA)s, %(TITULO)s, %(DATA_ATUALIZACAO)s, %(HORA_ATUALIZACAO)s)")
	for noticia in registros:
		dados_noticia = {
			'ID': noticia['id'],
			'FONTE': noticia['fonte'],
			'EDITORIA': noticia['editoria'],
			'TITULO': noticia['titulo'],
			'DATA_ATUALIZACAO': noticia['data_atualizacao'],
			'HORA_ATUALIZACAO': noticia['hora_atualizacao']
		}
		cursor.execute(add_noticia, dados_noticia)

	conexao.commit()
	cursor.close()
	conexao.close()