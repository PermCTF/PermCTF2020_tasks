<?php
session_start();

if ($_POST['login'] == "admin" and  $_POST['password'] == "admin" ) {
		echo  "<p> Welcome to home, Admin</p>";
				echo "<p> PermCTF{stay_away_from_default_passwords}</p>" ;
				        echo '<img src="respect.jpg" align="middle"<img>';
}
else {
		 exit("Access denied");
}

?>

