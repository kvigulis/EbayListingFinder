<?php
    require_once 'login.php';
    $conn = new mysqli($hn, $un, $pw, $db);
    if ($conn->connect_error) die($conn->connect_error);

    $query = "SELECT * FROM laserLinks";
    $result = $conn->query($query);
    if(!$result) die($conn->error);

    $rows = $result->num_rows;
?>
    <table cellspacing="0" cellpadding="0" border="0" width="800">
 	<tr>
  	<td>
   	<table cellspacing="0" cellpadding="1" border="1" width="800" >
   	<col width="121">
   	<col width="146">
  	<col width="117">
  	<col width="600">
     <tr style="color:white;background-color:grey">
     	<th>Time Found</th> 
        <th>Image</th>        
        <th>Price</th>
        <th>Title</th>
     </tr>
   </table>
  </td>
 </tr>
<tr>
<td>
   	<div style="width:800px; height:600px; overflow:auto;">
    <table cellspacing="0" cellpadding="1" border="1" width="800" >
    <col width="120">
    <col width="120">
  	<col width="120">
  	<col width="600">
        <tr>
        <?php
        for ($j = 0; $j < $rows ; ++$j)
    	{
    		$result->data_seek($j);
    		$row = $result->fetch_array(MYSQLI_ASSOC);
    		echo '<tr>'; // Start new row in the table.    		
    		echo '<td>'. gmdate("Y-m-d\ H:i:s", $row['time']).'</td>';
    		echo '<td><a href='.$row['URL'].'> <img src='.$row['imageURL'].' alt="Item" style="width:120px;height:120px;"></a></td>'; 
			echo '<td style="text-align:center"><b>£ '. $row['price'].'</td>'; 
    		echo '<td><a href='.$row['URL'].'>'. $row['title'].'</a></td>';    		
        	echo '</tr>'; // Close current row.
        }
        ?>
        </tr>      
    </table>  
   </div>
  </td>
 </tr>
</table>

