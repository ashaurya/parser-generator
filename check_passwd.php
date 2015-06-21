<?php session_start();

$_SESSION['incorrect'] = 0;
$user=$_POST['username'];
$password=$_POST['password'];
if($user=='admin' and $password=='what')
{
	$_SESSION['loggedin']='true';
	$_SESSION['username']=$user;
	$_SESSION['uuid']=1;
	header("location:main.php");
}
else
{
	$_SESSION['incorrect'] = 1;
	header("location:login.php");
}
?>
