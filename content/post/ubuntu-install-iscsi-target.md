+++
date = "2015-11-17T23:14:40+08:00"
draft = true
title = "Ubuntu搭建iscsi-target"

+++

## 介绍

使用Ubuntu可以搭建iSCSI服务器。

## 搭建步骤

### 初始化虚拟机

创建虚拟机，选择Ubuntu 14.04镜像。

绑定公网IP。

修改源，获得更好的下载速度。

```
apt-get update -y
```

### 安装软件

```
sudo apt-get install iscsitarget iscsitarget-dkms
```

### 启动服务

```
vim /etc/default/iscsitarget

ISCSITARGET_ENABLE=true

service iscsitarget restart

service iscsitarget status
```

### 创建LUN

```
mkdir -p /media/volume0

dd if=/dev/zero of=/media/volume0/storlun0.bin count=0 obs=1 seek=1G
```

### 创建target

添加LUN配置到配置文件。

```
vim /etc/iet/ietd.conf

Target iqn.2012-05.local.mynet:storage.sys0

Lun 0 Path=/media/volume0/storlun0.bin,Type=fileio,ScsiId=lun0,ScsiSN=lun0
```

### 然后重启服务。

```
sudo service iscsitarget restart
```

## 参考文档

<https://linhost.info/2012/05/configure-ubuntu-to-serve-as-an-iscsi-target/>
