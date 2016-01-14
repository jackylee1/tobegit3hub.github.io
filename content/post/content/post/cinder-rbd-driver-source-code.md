+++
date = "2015-12-04T23:55:52+08:00"
draft = true
title = "Cinder RBD驱动实现代码"

+++

## 介绍

Cinder很早就支持RBD驱动了，可以将Ceph作为块设备服务的后端，这是通过Cinder源码中的RBD driver实现的。

##源码分析

RBD驱动的源码在/cinder/volume/drivers/rbd.py，其中RBDDriver继承BaseVD，必须实现以下基本函数。

```
check_for_setup_error(self)

create_volume(self, volume)

delete_volume(self, volume)

ensure_export(self, context, volume)

create_export(self, context, volume, connector)

remove_export(self, context, volume)

initialize_connection(self, volume, connector, initiator_data=None)

terminate_connection(self, volume, connector, **kwargs)
```

由于RBDDriver也继承了TransferVD、ExtendVD、CloneableImageVD、SnapshotVD、MigrateVD，因此也必须实现以下的函数。

```
extend_volume(self, volume, new_size)

clone_image(self, volume, image_location, image_id, image_meta, image_service)

create_snapshot(self, snapshot)

delete_snapshot(self, snapshot)

create_volume_from_snapshot(self, volume, snapshot)

migrate_volume(self, context, volume, host)
```

这个驱动还实现了很多工具类，我们不逐一分析，就以最重要的create_volume和delete_volume为例子串通整个流程吧。

当用户通过命令行或API创建卷时，cinder-api接受请求，转发给cinder-scheduler，然后发给后端任意一个cinder-volume，这时根据配置文件指定的RBD后端请求/cinder/volume/drivers/rbd.py的create_volume()。

首先获取传入的volume大小参数，然后根据配置文件指定的chunk大小，计算出rbd的order。

然后是创建RADOSClient，这个客户端在初始化时会连RADOS，这是使用ceph官方的python库，通过配置文件写好的账号信息来返回一个ioctx。

有了ioctx，我们还是创建一个新的RBDProxy，这是一个标准的eventlet tpool。

最后使用ceph官方的python rbd库来调用create()。

至于delete_volume的逻辑相对复杂些，先通过rbd库获取Image对象，然后这个Image的所有backup，最后通过RBDProxy调用接口来删除。
