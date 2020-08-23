<?php
// # 记录请求
// $myfile = fopen("newfile.txt", "a") or die("Unable to open file!");
// $txt = "[GET]" . http_build_query($_GET,'',', ') . "\n";
// fwrite($myfile, $txt);
// $txt = "[POST]" . http_build_query($_POST,'',', ') . "\n";
// fwrite($myfile, $txt);
// $txt = "[HEADERS]" . http_build_query($_SERVER,'',', ') . "\n";
// fwrite($myfile, $txt);
// fclose($myfile);

# 未设置请求参数不给请求
if(!isset($_GET['uri'])){
	die("BT crack server 1.0");
}

$base_url = 'http://119.147.144.34';

# 判断GET参数
if($_GET['uri'] == "/api/panel/get_soft_list" || $_GET['uri'] == "/api/panel/get_soft_list_test") {
	$ch = curl_init(); 
	$httpHeader = ['Host: www.bt.cn'];
	// set url 
	curl_setopt($ch, CURLOPT_URL, $base_url . $_GET['uri']); 
	//return the transfer as a string 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $httpHeader);
	curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($_POST));
	// $output contains the output string 
	$output = curl_exec($ch);
	$output = json_decode($output, true);
	
	foreach ($output['list'] as $key => &$value) {
		# 付费插件全部到期日期修改
		if(floatval($value['pid']) > 0){
			$value['endtime'] = 253402185600;
		}
	}
	$output['pro'] = 0;
	$output['ltd'] = 1;
	
	// 返回JSON_ENCODE
	echo(json_encode($output));
	// close curl resource to free up system resources 
	curl_close($ch); 
}elseif ($_GET['uri'] == "/api/Plugin/check_plugin_status") {
	$output['status'] = true;
	
	// 返回JSON_ENCODE
	echo(json_encode($output));
}elseif ($_GET['uri'] == "/api/panel/plugin_total"){
	echo("1");
}elseif ($_GET['uri'] == "/api/coll/get_coll_plugin_list"){
	$ch = curl_init(); 
	$httpHeader = ['Host: www.bt.cn'];
	// set url 
	curl_setopt($ch, CURLOPT_URL, $base_url . $_GET['uri']); 
	//return the transfer as a string 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $httpHeader);
	curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($_POST));
	// $output contains the output string 
	$output = curl_exec($ch);
	$output = json_decode($output, true);
	
	$output['num'] = 99999;
	$output['endtime'] = 253402185600;
	
	// # 记录请求
	// $myfile = fopen("newfile.txt", "a") or die("Unable to open file!");
	// $txt = "[DATA]" . json_encode($output) . "\n";
	// fwrite($myfile, $txt);
	// fclose($myfile);
	
	// 返回JSON_ENCODE
	echo(json_encode($output));
	// close curl resource to free up system resources 
	curl_close($ch); 
}elseif ($_GET['uri'] == "/api/cloudtro/get_product_order_status"){
	$ch = curl_init(); 
	$httpHeader = ['Host: www.bt.cn'];
	// set url 
	curl_setopt($ch, CURLOPT_URL, $base_url . $_GET['uri']); 
	//return the transfer as a string 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $httpHeader);
	curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($_POST));
	// $output contains the output string 
	$output = curl_exec($ch);
	$output = json_decode($output, true);
	
	
	if($_POST['uid'] != 0){
		$output['status'] = true;
		$output['msg'] = [];
		$output['msg']['endtime'] = 253402185600;
		$output['msg']['num'] = 99999;
	}
	
	// # 记录请求
	// $myfile = fopen("newfile.txt", "a") or die("Unable to open file!");
	// $txt = "[DATA]" . json_encode($output) . "\n";
	// fwrite($myfile, $txt);
	// fclose($myfile);
	
	// 返回JSON_ENCODE
	echo(json_encode($output));
	// close curl resource to free up system resources 
	curl_close($ch); 
}
?>