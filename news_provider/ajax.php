<?php

function open_database() {
	try {
		$conn = new mysqli($_ENV['MYSQL_HOST'], $_ENV['MYSQL_USER'], $_ENV['MYSQL_PASS'], $_ENV['MYSQL_DATABASE']);
		mysqli_set_charset($conn,"utf8");
		return $conn;
	} catch (Exception $e) {
		echo $e->getMessage();
		return null;
	}
}
function close_database($conn) {
	try {
		mysqli_close($conn);
	} catch (Exception $e) {
		return $e->getMessage();
	}
	return '';
}
$conn = open_database();
$sql = 'SELECT EDITORIA, FONTE, TITULO FROM `noticias` WHERE DATA_ATUALIZACAO = CURRENT_DATE ORDER BY RAND() LIMIT 1';
$result = $conn->query($sql);
$row = $result->fetch_assoc();
close_database($conn);

echo json_encode($row);

?>