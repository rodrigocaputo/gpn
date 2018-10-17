var numero = -1;
var quadro = 0;
	var contador = 0;
function trocarQuadro() {
	var antigo = 'quadro' + quadro;
	quadro = (quadro + 1) % 2;
	var novo = 'quadro' + quadro;
	$('#' + antigo).css({'opacity': 0.5, 'z-index': 0});
	numero = ((numero + 1) % 3);
	if (document.getElementById(novo).src == '') {
		setTimeout(function(){trocarQuadro();}, 15000);
	} else {
		document.getElementById(novo).play();
	}
	$('#' + novo).css({'opacity': 1, 'z-index': 1});
	var url = document.getElementById(novo).src;
	if (url == '') {
		url = document.getElementById(novo).poster;
	}
	url = (url.substr(url.indexOf('media/') + 6));
	$.ajax({
		url: 'proximo_video.php',
		data: {'anterior': url},
		dataType: 'json',
		success: function(data){
			var tipo = 'video';
			if (data.indexOf('.mp') < 0) {
				document.getElementById(antigo).removeAttribute('src');
				document.getElementById(antigo).poster = 'media/' + data;
			} else {
				document.getElementById(antigo).src = 'media/' + data;
				document.getElementById(antigo).removeAttribute('poster');
				document.getElementById(antigo).onended = function(){trocarQuadro();};
			}
			document.getElementById(antigo).load();
		}
	});
}
window.onload = function(){
	trocarQuadro();
}