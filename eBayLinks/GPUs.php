<?php
    require_once 'login.php';
    $conn = new mysqli($hn, $un, $pw, $db);
    if ($conn->connect_error) die($conn->connect_error);      
?>

<head>
  <title>eBay Miner - Industrial Lasers</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<div class="jumbotron text-center">
  <h1>eBay Gem Miner</h1>  
  <p>Displays customized automatic searches for very specific eBay listings.</p> 
</div>
  
<div class="container">
  <div class="row">
    <div class="col-sm-3">
      <a href="Lasers.php"><h3>Industrial Lasers</h3></a>
      <p>Minimum Power: 150W</p>
      <p>Max Price: £5000</p>
    </div>
    <div class="col-sm-3">
      <a href="Oscilloscopes.php"><h3>Oscilloscopes</h3></a>       
      <p>Max Price: £200</p>      
    </div>
    <div class="col-sm-3">
      <a href="Z97.php"><h3>Z97 MOBOs</h3></a>
      <p>Max Price: £20</p>      
    </div>    
    <div class="col-sm-3">
      <a href="GPUs.php"><h3>GPUs</h3></a>   
      <p>Max Price: £300</p>       
      <p>NVidia 1070 GTX and 1080 GTX</p>      
    </div>
  </div>
</div>
</body>

<table class="table table-bordered">
  <thead>
    <tr>
     	<th>Time Found</th> 
      <th>Image</th>        
      <th>Price</th>
      <th>Title</th>
    </tr>  
  </thead>
  <tbody>
        <?php        
        $query = "SELECT * FROM GPULinks ORDER BY time DESC";
        $result = $conn->query($query);
        if(!$result) die($conn->error);        

        $rows = $result->num_rows;

        for ($j = 0; $j < $rows ; ++$j)
    	  {
    		$result->data_seek($j);
    		$row = $result->fetch_array(MYSQLI_ASSOC);
    		echo '<tr>'; // Start new row in the table.    		
    		echo '<td>'. gmdate("Y-m-d\ H:i:s", $row['time']).'</td>';
    		echo '<td><a href='.$row['URL'].'> <img src='.$row['imageURL'].' alt="Item" ></a></td>'; 
			  echo '<td style="text-align:center; vertical-align: middle; white-space: nowrap" ><b>£ '. number_format($row['price'],2).'</td>'; 
    		echo '<td><a href='.$row['URL'].'>'. $row['title'].'</a></td>';    		
        echo '</tr>'; // Close current row.
        }
        ?>   
 </tbody>
</table>