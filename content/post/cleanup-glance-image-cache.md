+++
date = "2015-11-10T09:00:03+08:00"
draft = true
title = "Glance清理cache image"

+++

## 介绍

OpenStack使用Ceph分布式存储后，理论上不需要cache image了，在部署时可以修改这个配置，对于已经有cache image的可以通过以下的方法清理。

## 清理数据库

```
glance-cache-manage -f delete-all-cached-images

glance-cache-manage list-cached
```

## 删除缓存文件

清理/var/lib/glance/image-cache/下的缓存文件。
