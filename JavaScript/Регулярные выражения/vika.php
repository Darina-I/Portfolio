<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title> 5 лаба</title>
</head>
<body>
<form method="POST">
<h3>Введите строку</h1>
<input type="text" name = "str">
<input type="submit" value="Отправить">
</form>
<?php
error_reporting(-1);
header('Content-Type: text/html; charset=utf-8');
mb_internal_encoding("UTF-8");
$reg="/^([а-яА-Я]+[ ]*)*\.$/u";
echo "preg = ". preg_match($reg, $_POST["str"]). "<br>";
if (isset($_POST["str"]) && preg_match($reg, $_POST["str"]) ) {
$str = $_POST["str"];
$strD = mb_substr($str, 0, -1, "UTF-8");
echo $strD."<br>";
$s = preg_split("/[ ]+/", $strD); // разбиваем на слова
$world = array();
echo "s[0] = ".$s[0]."<br>";
echo "count s = ". count($s). "<br>";
$count = count($s);
for ($i=0; $i < $count; $i++) {
$strTmp = $s[$i];
echo "strTmp = ". $strTmp . "<br>";
$reverse = '';
$z = 0;
while(!empty($strTmp[$z])){
echo "strTmp[z] = ". $strTmp[$z]. "<br>";
echo " reverse = str[z].reverse =". $strTmp[$z].$reverse. "<br>";
$reverse = $strTmp[$z].$reverse;
$z++;
}
//echo "reverse = ". $reverse. "<br>";
//echo "strTmp = ". $strTmp. "<br>";
if (mb_strtolower($strTmp)==mb_strtolower($reverse)) {
array_push($world, $strTmp);
}
//else echo "NO";
}
echo implode(' ',$world);
}
else echo "Введите корректно";
?>


</body>
</html>