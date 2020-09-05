<?php
function posturl($url,$data,$headerArray){
    $data  = json_encode($data);
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST,FALSE);
    curl_setopt($curl, CURLOPT_POST, 1);
    curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
    curl_setopt($curl,CURLOPT_HTTPHEADER,$headerArray);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    $output = curl_exec($curl);
    curl_close($curl);
    return json_decode($output);

}

$url = "https://openapi.mp.usr.cn/usrCloud/datadic/getDatas";
$jsonStr = array(
    "deviceId" => "00018403000000000005",
    "slaveIndex" =>"1",
    "sortByWeight" => "up"
);
$login_jsonStr = array("account" => "LCG", "password" => "4bb5c699a308f8ec29202321ea798400");
$login_url = "https://openapi.mp.usr.cn/usrCloud/user/login";
$login_headerArray = array('Content-Type: application/json');
$token = posturl($login_url,$login_jsonStr,$login_headerArray)->data->token;
$headerArray = array('Content-Type: application/json','token:'.$token);
//var_dump(posturl($url,$jsonStr,$headerArray));
$num = count(posturl($url,$jsonStr,$headerArray)->data->iotDataDescriptionList);
for($i=0; $i<=$num; $i++){
    print_r(posturl($url,$jsonStr,$headerArray)->data->iotDataDescriptionList[$i]->name);
}
?>