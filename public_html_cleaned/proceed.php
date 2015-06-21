<?php session_start();
if(!isset($_SESSION['username']))
header("location:index.php");
?> 
<?php 
$data=$_POST['data'];
$exp=$_POST['exp'];
$grammar=$_POST['grammar'];
if((isset($_POST['data'])) && !empty($_POST['data']))
{
	$upload=0;
}
else 
{
	$upload=1;
}
if((isset($_POST['exp'])) && !empty($_POST['exp']))
{
	$uploadexp=0;
}
else 
{
	$uploadexp=1;
}
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<script type="text/javascript" src="jquery.js"></script>
<style type="text/css">
h1 {font-size:140%;color:#0000CE;background-color:rgb(59, 89, 152); text-align:center; color:white;padding-top:1%; padding-bottom:1%;}
h2 {font-size:100%;color:#0000CE;background-color:rgb(59, 89, 152); text-align:center; color:white;padding-top:1%; padding-bottom:1%;}
td {padding-left: 10px; padding-right: 10px;}
table {-moz-border-radius: 10px;-webkit-border-radius: 10px;background-color:#FFFFC8;}
.content {padding-top: 10px; padding-left: 25px; padding-bottom: 10px; border-style:solid;border-radius:10px;border-width:1px;margin-top:5px;-moz-box-shadow: 0 0 5px 5px rgba(180,180,180,0.5);-webkit-box-shadow: 0 0 5px 5px rgba(180,180,180,0.5);width: 270px;}
.tab-box a {
  border:1px solid #DDD;
  color:#666666;
  padding: 5px 15px;
  text-decoration:none;
  background-color: #eee;
}
.tab-box a.activeLink { 
  background-color: #fff; 
  border-bottom: 0; 
  padding: 6px 15px;
}
.tabcontent { border: 1px solid #ddd; border-top: 0; padding: 5px;}
.hide { display: none;}

.small { color: #999; margin-top: 100px; border: 1px solid #EEE; padding: 5px; font-size: 9px; font-family:Verdana, Arial, Helvetica, sans-serif; }
</style>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta http-equiv="content-language" content="en-US">
<meta http-equiv="cache-control" content="no-cache">
<title>ParseGen</title>

<script type="text/javascript">
  $(document).ready(function() {
    $(".tabLink").each(function(){
      $(this).click(function(){
        tabeId = $(this).attr('id');
        $(".tabLink").removeClass("activeLink");
        $(this).addClass("activeLink");
        $(".tabcontent").addClass("hide");
        $("#"+tabeId+"-1").removeClass("hide")   
        return false;	  
      });
    });  
  });
</script>

</head>
<body style='font-family:sans-serif;font-size:14;margin:auto;width:940px;background:#BBDAFF;'>
  <div id="user" align="right">
    	<ul>
	<li>Hi, <?php echo $_SESSION['username'];?></li> 
	<li> <a href="logout.php">Logout</a> </li>
	<li> <a href="main.php">Back</a> </li>
	</ul>
   </div>
  <div class="tab-box"> 
      <a href="javascript:;" class="tabLink activeLink" id="cont-1">Rules</a> 
      <a href="javascript:;" class="tabLink " id="cont-2">First and Follow Sets</a> 
      <a href="javascript:;" class="tabLink " id="cont-3">LL(1) Parse Table</a> 
      <a href="javascript:;" class="tabLink " id="cont-4">LR(0)</a> 
      <a href="javascript:;" class="tabLink " id="cont-6">SLR(1)</a> 
      <a href="javascript:;" class="tabLink " id="cont-5">LR(1)</a> 
      <a href="javascript:;" class="tabLink " id="cont-7">LALR(1)</a> 
      <a href="javascript:;" class="tabLink " id="cont-8">Parsing</a> 
  </div>
<?php
if ($upload==1 && ($_FILES["file"]["type"] == "text/plain") && ($_FILES["file"]["size"] < 1000))
  {
  if ($_FILES["file"]["error"] > 0)
    {
    echo "Return Code: " . $_FILES["file"]["error"] . "<br />";
    }
  else
    {
    move_uploaded_file($_FILES["file"]["tmp_name"],"input.txt");
    }
  }
if ($uploadexp==1 && ($_FILES["file_exp"]["type"] == "text/plain") and ($_FILES["file_exp"]["size"] < 10000))
  {
  if ($_FILES["file_exp"]["error"] > 0)
    {
    echo "Return Code: " . $_FILES["file_exp"]["error"] . "<br />";
    }
  else
    {
    move_uploaded_file($_FILES["file_exp"]["tmp_name"],"expression.txt");
    }
  }
$first=0;
$follow=0;
$closure=0;
$parse_table=0;
$action_table=0;
$parse=0;
$lrclosure=0;
$lraction_table=0;
$lrparse=0;
$laclosure=0;
if(isset($_POST['first']) && $_POST['first'] == 'First Set')
{
	$first=1;
}
if(isset($_POST['follow']) && $_POST['follow'] == 'Follow Set')
{
	$follow=1;
}
if(isset($_POST['closure']) && $_POST['closure'] == 'Closure Set')
{
	$closure=1;
}
if(isset($_POST['parse_table']) &&    $_POST['parse_table'] == 'Parse Table')
{
	$parse_table=1;
}
if(isset($_POST['action_table']) &&    $_POST['action_table'] == 'Action Table')
{
	$action_table=1;
}
if(isset($_POST['lrclosure']) && $_POST['lrclosure'] == 'LR(1) Closure Set')
{
	$lrclosure=1;
}
if(isset($_POST['lraction_table']) &&    $_POST['lraction_table'] == 'LR(1) Action Table')
{
	$lraction_table=1;
}
if(isset($_POST['parse']) &&    $_POST['parse'] == 'parse')
{
	$parse=1;
}
if(isset($_POST['lrparse']) &&    $_POST['lrparse'] == 'lrparse')
{
	$lrparse=1;
}
if(isset($_POST['laclosure']) && $_POST['laclosure'] == 'LALR Closure Set')
{
	$laclosure=1;
}
if($upload==0)
{	
$file = "input.txt";
$fp = fopen($file, 'w');
fwrite($fp, $data);
fclose($fp);
}
if($uploadexp==0)
{
$file1 = "expression.txt";
$fp1 = fopen($file1, 'w');
fwrite($fp1, $exp);
fclose($fp1);
}
if($_POST['grammar']!='none')
{
	copy("grammar/$grammar","input.txt");
}
$command2 = "/usr/bin/python2 parser.py $first $follow $closure $parse_table $action_table $parse $lrclosure $lraction_table $lrparse $laclosure < input.txt";
$temp2 = shell_exec($command2);
print $temp2;
$fileout = "output.txt";
$f = fopen($fileout, 'w');
fwrite($f, $temp);
fclose($f);

$done=unlink("input.txt");
$done=unlink("expression.txt");
?>
<center><a href="#" > Back to top </a></center>

</body>
</html>
