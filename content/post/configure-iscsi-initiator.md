+++
date = "2015-12-11T23:11:49+08:00"
draft = true
title = "配置iSCSI Initiator"

+++

## 介绍

iSCSI Initiator可以理解是iSCSI存储的客户端，连接存储服务后发现块设备，并且像本地硬盘一样使用块设备。

## 配置步骤

本文介绍在Ubuntu配置iSCSI Initiator，并且login到远端的iSCSI target服务中。

## 安装open-iscsi

sudo apt-get install open-iscsi

## 发现target

iscsiadm -m discovery -t sendtargets -p 10.0.0.194

## 登录target

iscsiadm -m node -Tiqn.2006-01.com.openfiler:tsn.a489d138c0d9 -p 10.0.0.194 --login

## 查看块设备

lsblk

## 使用LVM格式化

参考LVM介绍

## 登出target

iscsiadm -m node -Tiqn.2006-01.com.openfiler:tsn.a489d138c0d9 -p 10.0.0.194 --logout

## 查看服务状态

/etc/init.d/open-iscsi status
