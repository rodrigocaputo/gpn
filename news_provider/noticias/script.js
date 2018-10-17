var exibeNoticia = function (editoria, fonte, titulo) {
	$('#editoria').animate({opacity: 0}, 250, function() {
		$(this).html(editoria);
		$(this).animate({opacity: 1}, 750);
	});
	$('#fonte').animate({opacity: 0}, 250, function() {
		$(this).html(fonte);
		$(this).animate({opacity: 1}, 750);
	});
	$('#texto').animate({opacity: 0}, 250, function() {
		$(this).html(titulo);
		$(this).animate({opacity: 1}, 750);
	});
}
var trocaNoticia = function () {
	$.ajax({
		type: 'GET',
		url: 'ajax.php',
		timeout: 3000,
		datatype: 'JSON',
		contentType: "application/json; charset=utf-8",
		cache: false,
		success: function(json) {
			if (json != 'null') {
				json = JSON.parse(json);
				exibeNoticia(json['EDITORIA'], 'Fonte: <b>' + json['FONTE'] + '</b>', json['TITULO']);
			} else {
				exibeNoticia('', '', 'Bem-vindo ao Sicoob Credivertentes!');
			}
		},
		error: function() {
			exibeNoticia('', '', 'Bem-vindo ao Sicoob Credivertentes!');
		}
	});
}
setInterval(trocaNoticia, 15000);