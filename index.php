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
<div id='header' style='width:75%;text-align:center;color:#0e4ead;padding-top:50px;padding-left:12.5%;font-size:40px;'>
	  <b>Parser Generator</b>
  </div>
<div id="main"><div id="login" style='margin:11% 20% 12% 44%;'>
<?php 
if(!isset($_SESSION['loggedin']))
{?>
<form id="data" method="POST" action="check_passwd.php">
<label for="username"><b>Username:</b></label>&nbsp;&nbsp;<input type="text" name="username" id="username"><br>
<label for="password"><b>Password:</b></label>&nbsp;&nbsp;<input type="password" name="password" id="password">
<br>

<?php	
if($_SESSION['incorrect'] == 1)
	echo "<p style=\"color:red;\">Incorrect id or password!</p>";
?>

<br />
<input type="submit" value="Login" id="Login" style='margin-left:32%'> 
<?php } else
header("location:main.php");?>
</div>
</div>
</body>
</html>
