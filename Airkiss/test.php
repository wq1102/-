<?php
$verify = $_GET["verify"];
header('content-type:json');
echo json_encode($verify);
?>