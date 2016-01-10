+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "nginx log service"

+++



## 简介

我们需要对外提供简单的Log服务，让开发者可以下载服务器上的日志文件，通过Nginx可以做权限管理和静态文件服务。

做这个简单的服务只需要安装下Nginx，做好相关配置就可以了。

## Nginx-log-service

基于Nginx的Log服务配置和使用方法已经托管到[Github](https://github.com/tobegit3hub/nginx-log-service)。

安装好Nginx后，用htpasswd生成账号密码文件，拷贝nginx.conf到指定目录，启动Nginx即可。亲测应该没坑。



