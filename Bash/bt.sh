#!/bin/bash

echo "本脚本由老兄制作,仅供研究使用"
echo "我的博客:https://www.moec.top"
echo "请在运行前提前安装curl"
echo "------------------------"
echo "1.开始运行"
echo "2.添加hosts文件保护"
echo "3.取消hosts文件保护"
echo "4.退出"
echo "------------------------"

echo "请输入命令:"
read choice
case $choice in
	1)
	mkdir /www/server/panel/vhost/cert/www.bt.cn -p
	mkdir /www/wwwroot/www.bt.cn -p
	curl https://raw.githubusercontent.com/laoxong/lxongOther/master/bt/bt.php -o /www/wwwroot/www.bt.cn/bt.php
	curl https://raw.githubusercontent.com/laoxong/lxongOther/master/bt/www.bt.cn.conf -o /www/server/panel/vhost/nginx/www.bt.cn.conf
	curl https://raw.githubusercontent.com/laoxong/lxongOther/master/bt/ssl/privkey.pem -o /www/server/panel/vhost/cert/www.bt.cn/key.key
	curl https://raw.githubusercontent.com/laoxong/lxongOther/master/bt/ssl/fullchain.pem -o /www/server/panel/vhost/cert/www.bt.cn/bt.pem
	chown www:www /www/wwwroot/www.bt.cn/* -R
	/etc/init.d/nginx reload
	echo "127.0.0.1 www.bt.cn" >> /etc/hosts
	chattr +i /etc/hosts
	echo "完成!"
	echo "请手动更新下软件列表"
	;;

	2)
	chattr +i /etc/hosts
	echo "已经添加hosts文件保护"
	echo "如果您要修改hosts文件,请先取消保护"
	;;

	3)
	chattr -i /etc/hosts
	echo "hosts文件保护已经取消"
	;;

	4)
	break
	;;

	*)
	echo "你什么都不输入你到底想让我干什么..."
	;;
esac 