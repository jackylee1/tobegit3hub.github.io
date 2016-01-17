+++
date = "2015-11-15T08:58:46+08:00"
draft = true
title = "配置Glance关闭cache image"

+++

## 介绍

OpenStack使用分布式存储Ceph后，就不需要Glance的cache image了，我们可以通过修改配置文件来关闭这个功能。

## 修改配置

修改Glance配置文件/etc/glance/glance-api.conf。

默认配置项是：

```
[paste_deploy]

flavor=keystone+cachemanagement
```

修改配置项为：

```
[paste_deploy]

flavor=keystone
```

然后重启glance-api和（如果是Juno或以前版本）glance-registry。

## 参考文档

http://www.sebastien-han.fr/blog/2014/11/03/openstack-glance-disable-cache-management-while-using-ceph-rbd/
