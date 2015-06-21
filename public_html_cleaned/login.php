<?php session_start();?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta http-equiv="content-language" content="en-US">
<meta http-equiv="cache-control" content="no-cache">
<title>ParseGen</title>
<script src="jquery.js" type="text/javascript"></script>
<script src="javascript.js" type="text/javascript"></script>
<style>
@import url("login_style.css");
</style>
</head>
<body>
<div id="main"><div id="login">
<?php 
if(!isset($_SESSION['loggedin']))
{?>
<form id="data" method="POST" action="check_passwd.php">
<label for="username">Username:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="username" id="username"><br>
<label for="password">Password: </label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="password" name="password" id="password">
<br>

<?php	
if($_SESSION['incorrect'] == 1)
	echo "<p style=\"color:red;\">Incorrect id or password!</p>";
?>


<input type="submit" value="Login" id="Login"> 
<?php } else
header("location:main.php");?>
</div>
</div>
</body>
</html>
