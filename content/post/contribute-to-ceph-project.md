+++
date = "2015-06-28T08:35:33+08:00"
draft = true
title = "contribute to ceph project"

+++



## Ceph简介

Ceph是开源的分布式统一存储系统，提供对象存储、块设备存储以及文件系统服务。

基于Ceph的统一存储方案受到越来越多基础服务厂商关注，雅虎基于对象存储组件RGW提供了类S3服务，UnitedStack及国内外OpenStack厂商基于RBD提供块设备服务（也就是云硬盘）和基于CephFS的网络文件系统服务。

![](/images/ceph_logo.png)

## Ceph社区

随着OpenStack社区的发展，Ceph从Sage Weil的博士论文一跃成为最流行的SDS存储解决方案。Ceph与OpenStack结合更是提供了S3、云硬盘、SAN等基础存储服务。

这两年Docker的兴起让容器成为行业的焦点，Ceph社区开始着手解决容器的数据持久化问题，目前已提供容器块设备以及集成Kubernetes持久卷等功能。

本文将介绍我为Ceph社区贡献的代码，也是与容器有关。

## 容器化Ceph

容器时对进程的封装，Docker为容器提供了非常易用的镜像描述语言，使用Docker可以封装Ceph的运行环境，让Ceph的开发和部署更加容易。Ceph社区也是对Docker支持最好的开源项目之一，包括OSD、Monitor、MDS和RGW等所有组件都提供了官方的Docker镜像，甚至集成了一个All in one的镜像让开发者可以在本地快速启动完整的Ceph服务，更详细的地址请移步Github https://github.com/ceph/ceph-docker

于此同时，Ceph项目包含了组件ceph-rest-api，这是为开发人员提供的Ceph监控管理服务，通过RESTful API的形式让运维人员能够远程或者可视化地操作Ceph集群。ceph-rest-api的启动方式也很简单，命令如下。

```
ceph-rest-api -n client.admin
```

遗憾的是，官方提供的All in one镜像里面并没有包含ceph-rest-api服务，用户如果想尝试这项功能，必须手动启动这个Demo容器，然后通过Docker命令进入容器后再启动。这其实是给了我们贡献代码的机会，虽然我可以本地Export一个带ceph-rest-api的镜像和容器，但为了让更多人也能享受容器带来的便利，我们觉得理应反馈给社区。

## 贡献代码

Ceph项目代码都托管在Github，同时使用Issues和Pull-request来管理社区，因此参与Ceph社区是非常容易的。于是我创建了本人在Ceph社区的第一个Issue，大家可以在下面的地址看到。

https://github.com/ceph/ceph-docker/issues/107

提出问题并且与社区确认问题后，我开始想着手解决这个问题了。研究了ceph-docker项目的Dockerfile和entrypoint.sh代码后，我添加了对ceph-rest-api的支持，在本地fork项目新建分支，然后点击创建pull-request。

https://github.com/ceph/ceph-docker/pull/108

隔日早起后发现，Ceph项目维护者给我提了Comment，需要修改Dockerfile并暴露5000端口。我很快确认了问题，然后重新commit，修复以后Ceph维护者很顺利得把我的代码Merge到官方仓库，然后出发Automated Build自动构建新的Ceph镜像。整个Patch从提交到review到修改到merge不到24小时，可以看出Ceph社区任然非常活跃，我们也欢迎更多开发者参与到Ceph社区。

## 最后

最后多说一下，在2014年Ceph社区贡献排行榜中Redhat高居全球第一，UnitedStack全球第二、国内第一，Ubuntu麒麟团队也有巨大贡献。Ceph社区也在考虑实现Key-value和NoSQL存储服务，一旦完成真正的统一存储时代将会来临，各位看官可不容错过啊！