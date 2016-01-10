+++
date = "2015-03-02T08:35:32+08:00"
draft = true
title = "reset mysql root password"

+++



* Stop MySQL

/etc/init.d/mysql stop

* Start with safe mode

mysqld_safe --skip-grant-tables &

* Login as root

mysql -u root

mysql> use mysql;
mysql> UPDATE user SET Password=PASSWORD("password") WHERE User='root';
mysql> flush privileges;
mysql> quit

* Stop MySQL

ps aux |grep mysql
kill -9 $pid

* Start MySQL

service mysql stop
service mysql start