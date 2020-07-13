#!/bin/sh
BAK_DIR="/data/backup/" #本机备份文件临时存储目录
WEB_DIR="/data/web/*" #要备份的网站文件
FTP_IP="xxx.xxx.xxx.xxx" #ftp地址
FTP_USER="username" #FTP用户名
FTP_PWD="password" #FTP密码
DATE_TIME=$(date +%F-%T)
DATE=$(date +%Y%m%d)
MYLOG_DIR='/var/log/mylogs'
mkdir -p /var/log/mylogs
DATE_TIME=$(date +%F-%T)
if [ -d BAK_DIR ]; then
chmod -R 755 $BAK_DIR
else
mkdir -p $BAK_DIR
chmod -R 755 $BAK_DIR
fi
#web backup
tar -zcPf $BAK_DIR/web_$DATE.tar.gz $WEB_DIR 2>&1
re1=$?
if [[ $re1 == 0 ]]; then
/bin/sync
/bin/sync
sleep 5
echo "Data has been completed package! $DATE_TIME" >> $MYLOG_DIR/databak.log

else
echo "Web completed package Fail!" >> $MYLOG_DIR/databak.log
fi
#Upload
if [[ $re1 == 0 ]] && [[ $re2 == 0 ]]; then
echo "Began to upload file $DATE_TIME" >> $MYLOG_DIR/databak.log
ftp -v -n $FTP_IP<<!
user $FTP_USER $FTP_PWD
binary
hash
cd /
lcd $BAK_DIR
prompt
mput *
close
bye
!
echo "Upload successful! $DATE_TIME" >> $MYLOG_DIR/databak.log
fi
rm -rf $BAK_DIR/*
