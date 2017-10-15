<html>
<head>
  <title>SAS</title>
</head>
<body style="background-color: black;">
<img id='button_red' src='data/img/red_button.jpg' onclick='window.location.href = "index.php?button=red";'/>
<img id='button_green' src='data/img/green_button.jpg' onclick='window.location.href = "index.php?button=green";'/>
<?php
$buttonstate = $_GET['button'];
if ($buttonstate == 'red') {
  shell_exec('sh /home/pi/SAS/scripts/lichtaus.sh');
}elseif ($buttonstate == 'green') {
  shell_exec('sh /home/pi/SAS/scripts/lichtein.sh');
}
?>
