+++
date = "2014-09-01T08:35:32+08:00"
draft = true
title = "standalone hbase on docker"

+++



Docker is becoming a more and more popular platform for developers. With docker you can run and develop any project easily. But how easy is it? I will take HBase as example.

1. First you should install [docker](http://docker.com/) by yourself.
2. Then run `docker run -d --name standalone-hbase -p 2181:2181 -p 16000:16000 -p 16010:16010 -p 16020:16020 -p 16030:16030 tobegit3hub/standalone-hbas`

Wow, that's all. You get a standalone HBase in your computer and you can monitor status on the browser. For more details, visit the [github repository](https://github.com/tobegit3hub/standalone-hbase) or the [docker image](https://registry.hub.docker.com/u/tobegit3hub/standalone-hbase/).

Docker should be useful for production. So I will deploy the HBase clusters on docker containers later.