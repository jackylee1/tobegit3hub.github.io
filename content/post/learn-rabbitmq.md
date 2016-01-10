+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "learn rabbitmq"

+++



## 运行RabbitMQ

```
docker run -d -e RABBITMQ_NODENAME=my-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

更多RabbitMQ容器信息在https://registry.hub.docker.com/_/rabbitmq/。

## 使用Web界面

打开http://host:15672，默认用户名guest密码guest。

## 写RabbitMQ客户端

开源代码实例 https://github.com/larrycai/codingwithme-rabbitmq

对应的教程PPT http://www.slideshare.net/larrycai/learn-rabbitmq-with-python-in-90mins

注意，需要把客户端连接的host改为“localhost”，如果使用容器才是“rabbit”。



