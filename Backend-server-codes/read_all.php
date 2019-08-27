<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");


//Creating Array for JSON response
$response = array();

// Include data base connect class
$filepath = realpath (dirname(__FILE__));
require_once($filepath."/db_connect.php");

 // Connecting to database
$db = new DB_CONNECT();

 // Fire SQL query to get all data from weather
$result = mysql_query("SELECT *FROM dust1") or die(mysql_error());

// Check for succesfull execution of query and no results found
if (mysql_num_rows($result) > 0) {

	// Storing the returned array in response
    $response["dust1"] = array();

	// While loop to store all the returned response in variable
    while ($row = mysql_fetch_array($result)) {
        // temperoary user array
        $dust1 = array();
        $dust1["id"] = $row["id"];
        $dust1["percent"] = $row["percent"];
		$dust1["levels"] = $row["levels"];

		// Push all the items
        array_push($response["dust1"], $dust1);
    }
    // On success
    $response["success"] = 1;

    // Show JSON response
    echo json_encode($response);
}
else
{
    // If no data is found
	$response["success"] = 0;
    $response["message"] = "No data found";

    // Show JSON response
    echo json_encode($response);
}
?>