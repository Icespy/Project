<?php
  
include('connect.php');
  
  if(isset($_GET['id'])) {
	  mysqli_query($objCon,"DELETE FROM users WHERE UserID = ".$_GET['id']);
  }

	$strSQL = "SELECT * FROM users ";
	$objQuery = mysqli_query($objCon,$strSQL);
  
?>
<html>
<head>
<title>Users Login</title>
<link rel="stylesheet" type="text/css" href="styleregis.css">
</head>
</head>
<body>

<div id="frm">
  <h2>UserInfo</h2><br>
  <table border="1" style="width: 300px">
    <tbody>
      <tr>
        <th>UserID</th>
        <th>Uername</th>
        <th>Password</th>
        <th>Name</th>
        <th>PhoneNumber</th>
        <th>Status</th>
        <th>tools</th>
      </tr>
      <?php
      while($objResult = mysqli_fetch_array($objQuery,MYSQLI_ASSOC)){
          ?>  
      <tr>
        <td><?php echo $objResult["UserID"];?></td>
        <td><?php echo $objResult["Username"];?></td>
        <td><?php $pass=md5($objResult["Password"]);
                  echo $pass;?></td>
        <td><?php echo $objResult["Name"];?></td>
        <td><?php echo $objResult["PhoneNumber"];?></td>
        <td><?php echo $objResult["Status"];?></td>
        <td>
            <a href="edit_profile.php?id=<?php echo $objResult["UserID"];?>">Edit</a>
            <a href="Showdatausers.php?id=<?php echo $objResult["UserID"];?>" onclick="return confirm('Do you want to delete this Users? !!!')">Delete</a>
        </td>
      </tr>
      <?php
      }
      ?>
    </tbody>
  </table>
  <br>
  <a href="admin_page.php"><input Type="submit" name="Submit" value="Back"></a></br>
</div>
</body>
</html>
<?php
mysqli_close($objCon);
?>