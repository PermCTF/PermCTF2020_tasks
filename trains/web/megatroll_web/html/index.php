<?php
session_start();
?>
<!DOCTYPE html>
<html>
	<head>
		<title>The Rabbit Hole</title>
		<style>

			body {
				text-align: center;
				padding: 40px 0;
				background-color: white;
			}

			input[type=submit]{
				 border: none;
				 padding: 16px 32px;
				 margin: 4px 2px;
				 cursor: pointer;
				 border-radius: 10px;
				 width: 180px;
			}

			button{
				background-color: lightgreen;
			}
					
		</style>
		
	</head>

	<body>
		<form action="security.php" method="post">
			<input name="login"    type="text"     size="15" maxlength="15" placeholder="Name">
			<input name="password" type="password" size="15" maxlength="15" placeholder="Password">
			<p><input type="submit" name="submit" value="Enter the dungeon"></p>
		</form>
	</body>
</html>
