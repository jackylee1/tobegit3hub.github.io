+++
date = "2015-12-04T08:56:25+08:00"
draft = true
title = "通过快照快速使用devstack"

+++

## 介绍

搭建devstack过程需要下载大量github项目和python库，在国内环境尤其容易失败，为了简化安装步骤，我们可以通过快照共享快速使用devstack。

## 准备快照

要有devstack快照，我们现在公有云创建虚拟机，然后按照无坑安装devstack来搭建devstack环境。

然后创建快照liberty-devstack，其中快照id是ba6c71cd-a0f7-4365-986f-d77b309056da。

## 共享快照

通过glance可以在后端共享镜像。

```
glance member-create ba6c71cd-a0f7-4365-986f-d77b309056da $tenant_id

glance member-list --image-id ba6c71cd-a0f7-4365-986f-d77b309056da
```

## 使用devstack

创建虚拟机，选择从快照中创建，选择liberty-devstack镜像。启动虚拟机后，切换stack用户，执行下面的命令即可。

```
su stack

cd ~/devstack

script /dev/null

./rejoin-stack.sh
```

绑定公网IP后，在浏览器就可以登陆，默认用户是admin和demo，密码是官方的nomoresecrete，这个镜像已经安装ceph，如果你想使用可以参考使用Docker部署单机版Ceph。

如果rejoin报错，可能还是devstack的问题，可参考devstack问题解决。