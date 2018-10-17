<?php

$anterior;
if (isset($_GET['anterior'])) {
	$anterior = utf8_decode(urldecode($_GET['anterior']));
}
$files = array_diff(scandir('media'), array('.', '..', '_.png'));
sort($files, SORT_NATURAL | SORT_FLAG_CASE);
if (in_array($anterior, $files)) {
	$continuar = true;
	while ($continuar) {
		if (current($files) === $anterior) {
			$continuar = false;
		}
		if (next($files) === false) {
			reset($files);
		}
		if (!$continuar) {
			echo(json_encode(utf8_encode(current($files))));
		}
	}
} else {
	echo(json_encode(array_pop($files)));
}

?>