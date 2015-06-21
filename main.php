<?php session_start();
if(!isset($_SESSION['username']))
header("location:index.php");
?> 

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta http-equiv="content-language" content="en-US">
<meta http-equiv="cache-control" content="no-cache">
<title>Parser</title>
</head>
<body style='font-family:sans-serif;font-size:14;margin-left:9%;width:75%;background:#BBDAFF;align:center;'>

<div id='header' style='width:75%;text-align:center;color:#0e4ead;padding-top:50px;padding-left:17.5%;font-size:40px;'>
<b>Parser Generator</b>
</div>

<div id="user" align="right">
<ul>
<li>Hi,<?php echo $_SESSION['username'];?></li> 
<li> <a href="logout.php">Logout</a> </li>
</ul>
</div>

<div id="main" style='width:100%;text-align:center;margin:auto;'>
<div id="login" style='float: left;font-family:arial;margin-left:15.5%;margin-top:1%;'>
<form id="data" method="POST" action="proceed.php" enctype="multipart/form-data" style='border-style:solid;border-radius:10px;border-width:1px;padding:10px 10px 5px 5px;margin-top:5px;-moz-box-shadow: 0 0 5px 5px rgba(180,180,180,0.5);-webkit-box-shadow: 0 0 5px 5px rgba(180,180,180,0.5);box-shadow: 0 0 5px 5px rgba(180,180,180,0.9);color:#0e4ead;background:#FFFFC8;'>
<h3>Input Grammar*:</h3>
<i><p style='font-size:14px;'>*Empty Strings must be wirtten as "epsilon" (without quotes)</i><br /></p>
<textarea style="color: black; background-color: #F0F8FF" rows="15" cols="100" name='data' id='data'></textarea><br />
or<br />
<label for="file">Upload Grammar file:</label><input type="file" name="file" id="file" /><br />
or<br />

Choose from Sample Grammars:<br/>
<select name="grammar" id="grammar" onchange="javascript:ShowDiv();">
<option value="none">None</option>
<option value="one">Sample Grammar 1</option>
<option value="two">Sample Grammar 2</option>
<option value="three">Sample Grammar 3</option>
<option value="four">Sample Grammar 4</option>
<option value="five">Sample Grammar 5</option>
<option value="six">Sample Grammar 6</option>
<option value="seven">Sample Grammar 7</option>
</select>
<!--ADD FROM HERE FOR DISPLAYING GRAMMAR line 45-161 -->
<center>
<div id="one" style="border:solid 1px black;width:300px;">
<BR><b>e: e '+' t
</b><BR><b>e: t
</b><BR><b>t: t '*' f
</b><BR><b>t: f
</b><BR><b>f: id
</b><BR><b>f: '(' e ')'
</b><BR><b></b><BR>	  </div>
<div id="two" style="border:solid 1px black;width:300px;">
<BR><b>bexpr: bexpr be
</b><BR><b>be: 'or' bterm be | 'epsilon'
</b><BR><b>bterm: bterm bt
</b><BR><b>bt: 'and' bfactor bt | 'epsilon'
</b><BR><b>bfactor: 'not' bfactor | '(' bexpr ')' | 'true' | 'false'
</b><BR><b></b><BR>	  </div>
<div id="three" style="border:solid 1px black;width:300px;">
<BR><b>expr: expr plus term 
</b><BR><b>expr: expr minus term 
</b><BR><b>expr: term
</b><BR><b>term: term mult fac 
</b><BR><b>term: term div fac 
</b><BR><b>term: fac
</b><BR><b>fac: lp expr rp 
</b><BR><b>fac: id
</b><BR><b>
</b><BR><b></b><BR>	  </div>
<div id="four" style="border:solid 1px black;width:300px;">
<BR><b>A : C x A 
</b><BR><b>A : 'epsilon'
</b><BR><b>B : x C y 
</b><BR><b>B : x C
</b><BR><b>C : x B x 
</b><BR><b>C : z
</b><BR><b></b><BR>	  </div>
<div id="five" style="border:solid 1px black;width:300px;">
<BR><b>S : F
</b><BR><b>S : '(' S '+' F ')'
</b><BR><b>F : a
</b><BR><b>
</b><BR><b></b><BR>	  </div>
<div id="six" style="border:solid 1px black;width:300px;">
<BR><b>S : a S a
</b><BR><b>S : b S b
</b><BR><b>S : a
</b><BR><b>S : b
</b><BR><b>S : 'epsilon'
</b><BR><b></b><BR>	  </div>
<div id="seven" style="border:solid 1px black;width:300px;">
<BR><b>S : a S a S b
</b><BR><b>S : a S b S a
</b><BR><b>S : b S a S a
</b><BR><b>S : 'epsilon'
</b><BR><b></b><BR>	  </div>
</center>

<script language="javascript">
function ShowDiv(){
safeToggleFieldDisplay(document.getElementById('one'),'none');
safeToggleFieldDisplay(document.getElementById('two'),'none');
safeToggleFieldDisplay(document.getElementById('three'),'none');
safeToggleFieldDisplay(document.getElementById('four'),'none');
safeToggleFieldDisplay(document.getElementById('five'),'none');
safeToggleFieldDisplay(document.getElementById('six'),'none');
safeToggleFieldDisplay(document.getElementById('seven'),'none');

var dropdown = document.getElementById("grammar");
var index = dropdown.selectedIndex;
var selectedDIV = dropdown.options[index].value;
safeToggleFieldDisplay(document.getElementById(selectedDIV),'flip');
}

function safeToggleFieldDisplay(field, sVisibility){
try{
if((field) && (field.style)){
if (sVisibility=='flip'){
if (field.style.display == 'none'){
sVisibility = 'block'; }
else {
sVisibility = 'none'; }
}
field.style.display = sVisibility;
}
}
catch(exception){
//no handling - just preventing page explosions
}
}

ShowDiv();
</script>
<!--END OF DISPLAYING GRAMMAR--> 
<br/><br/>
<h3>Input Expression to be parsed:</h3>
(Space separated expression)
<textarea style="color: black; background-color: #F0F8FF" rows="1" cols="100" name='exp' id='exp'></textarea><br />
or <br />
<label for="file_exp">Upload Expression file:</label><input type="file" name="file_exp" id="file_exp" /><br /><br />
<b>Parse Expression</b><br />
<input type="checkbox" name="parse" id="parse" value="parse">LR(0) Parse &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<input type="checkbox" name="lrparse" id="lrparse" value="lrparse">LR(1) Parse<br />
<input type="submit" value="Submit" id="ok" style='text-align:center;margin-top:10px;margin-bottom:15px;padding-top:2px;padding-bottom:2px;width:100px;font-size:14px;'>
</form>
<br />
</div>
<br /><br />
</div>
<br /><br />
</body>
</html>
