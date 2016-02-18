+++
date = "2016-02-13T12:26:53+08:00"
draft = true
title = "use alpine base docker image"

+++

## 介绍

在Docker官方博客中，已经明确未来将使用alpine作为官方镜像的base image，详情也可以通过这个博客了解到 <http://siliconangle.com/blog/2016/02/09/docker-gets-minimalist-with-plan-to-migrate-images-to-alpine-linux/> 。

Alpine是一个精简化的Linux镜像，使用自己实现的apk包管理系统，镜像小而且安全，可以从Github看到其源码 <https://github.com/gliderlabs/docker-alpine> 。目前作者已经加入Docker Inc，极力推动基础镜像的转换。详细介绍可参考官方文档 <http://gliderlabs.viewdocs.io/docker-alpine/> 和镜像文档 <https://hub.docker.com/_/alpine/> 。

## 使用例子

要使用apline作为base image也很简单，主要修改是不能使用apt-get或者yum，需要通过apk来安装依赖软件。

最简单的例子如下。

```
FROM alpine:3.1
RUN apk add --update mysql-client && rm -rf /var/cache/apk/*
ENTRYPOINT ["mysql"]
```

## Seagull使用alpine

在Seagull项目中也有开发者希望迁移到alpine base image，详见 <https://github.com/tobegit3hub/seagull/pull/62> 。

