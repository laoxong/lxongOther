 
#/bin/bash
#Gayhub:https://github.com/lixworth/CFBlockIP

#日志文件，你需要改成你自己的路径

logfile=/usr/local/caddy/log/
#结束时间现在

end_time=`date +%s`
#echo $end_time

#开始时间1分钟之前

start_time=$(( end_time - 60 ))
#echo $start_time

#过滤并统计日志中单位时间之内的最高ip数。请把$logfile/web.log替换为你的日志路径。

tac $logfile/web.log | awk -v st="$start_time" -v et="$end_time" '{if(($8 > st || $8 == st) && ($8 < et || $8 == et)) {print $3}}' | sort | uniq -c | sort -nr > $logfile/log_ip_top

ip_top=`cat $logfile/log_ip_top | head -1 | awk '{print $1}'`

#单位时间[1分钟]内相同ip访问次数超过 n 次自动加入到 Cloudflare 防火墙. （这里 5 次是做测试用的。）

ip=`cat $logfile/log_ip_top | awk '{if($1>5) print $2}'

# 填 Cloudflare 帐号的 Email 邮箱
CFEmail=""

# 填 Cloudflare 帐号的 Global API Key

GlobalAPIKey=""

# 填 Cloudflare 域名对应的 Zone ID

ZoneID=""

for IPAddr in $ip; do
if[$IPAddr -eq "127.0.0.1"]; then

else
for IPAddr in $ip; do
  if [ $IPAddr == "白名单IP" ]; then
    echo "none";
  else
    curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$ZoneID/firewall/access_rules/rules" \
      -H "X-Auth-Email: $CFEmail" \
      -H "X-Auth-Key: $GlobalAPIKey" \
      -H "Content-Type: application/json" \
      --data '{"mode":"block","configuration":{"target":"ip","value":"'$IPAddr'"},"notes":"CC/DDOS Attatch"}'  
  fi
done

