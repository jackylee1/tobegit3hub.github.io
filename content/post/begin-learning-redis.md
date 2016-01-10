+++
date = "2013-03-25T08:35:29+08:00"
draft = true
title = "begin learning redis"

+++



## Operation

* Best place to study,

* SET MyName “tobe”
* GET MyName
* DEL MyName
* SETNX is for SET if Not eXit
* INCR MyAge

* RPUSH for end of list and LPUSH for start
* LRANGE friends 0 -1
* LLen friends, maybe L for List and R for Reverse
* LPOP and RPOP

* SADD
* SREM
* SISMEMBER, SMEMBERS
* SUNION

* ZADD should give to number for sorting
* ZRANGE and z for sorted set

## 启动redis服务器和客户端

/src/redis-server
/src/redis-cli -h 127.0.0.1 -p 6379