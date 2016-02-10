+++
date = "2016-01-14T09:44:20+08:00"
draft = true
title = "使用Docker部署单机版Ceph"

+++

## 介绍

我们UOS使用Ceph作为Nova、Cinder、Glance的后端，为了通过devstack可以搭建OpenStack环境，但我们还需要快速搭建单机版Ceph。

在Ubuntu 14.04可以很方便搭建OpenStack，在同一台虚拟机搭建Ceph也很简单。

## 安装Docker

更新源可以安装较新版本的docker。

```
add-apt-repository -y ppa:docker-maint/testing

apt-get update -y

apt-get install -y docker.io
```

## 启动Ceph

通过ifconfig查看本地IP，假设为10.250.8.31，运行下面命令时需要替换IP。

```
docker run -d --net=host -v /etc/ceph:/etc/ceph -e MON_IP=10.250.8.31 -e CEPH_NETWORK=10.250.8.0/24 ceph/demo
```

为了简化安装步骤，你也可以直接执行下面三行命令。

```
local_ip=$(ifconfig eth0 | grep "inet addr" | awk -F : '{print $2}' | awk '{print $1}')

local_cidr=$(ipcalc -n $local_ip 255.255.255.0 | grep "Network" | awk '{print $2}')

sudo docker run -d --net=host -v /etc/ceph:/etc/ceph -e MON_IP=$local_ip -e CEPH_NETWORK=$local_cidr ceph/demo
```

## 测试Ceph

通过demo容器测试。

```
docker ps

docker exec -i -t a38f7b3ae7ca bash

rados lspools
```

安装和使用ceph命令。

```
apt-get install -y ceph

rados lspools
```