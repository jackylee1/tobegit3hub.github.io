+++
date = "2016-02-04T20:08:57+08:00"
draft = true
title = "Docker与Ceph集成"

+++

## 介绍

Ceph是流行的分布式存储，同时提供块设备、对象存储和文件系统三种接口，能为物理机、虚拟机甚至是容器提供可靠的持久存储。

Docker通过volume driver的方式可以对接Ceph，从而实现容器持久化数据卷的功能，也能轻易实现容器的迁移。

## 现状

Docker抽象出volume driver后，社区立即提Issue希望实现Ceph的plugin，详见地址 <https://github.com/docker/docker/issues/10661> 。而volume API实现的PR地址是 <https://github.com/docker/docker/issues/10661> 。

这个Issue很快就被close了，因为开源社区已经实现了功能代码，在项目volplugin中，项目地址 <https://github.com/contiv/volplugin> 。但这个项目是master/slave架构，还有单独的命令行工具来发送RESTful请求，还依赖etcd，显然不是轻量级的首选方案。除了这个项目，还有 <https://github.com/AcalephStorage/docker-volume-ceph-rbd> 和 <https://github.com/yp-engineering/rbd-docker-plugin> 实现了类似的功能，前者由于缺乏文档没有测试了，后者则有一篇比较详细的体验文档 <https://ceph.com/planet/getting-started-with-the-docker-rbd-volume-plugin/> 。

其实Kubernetes也可以直接使用RBD持久卷，实现原理类似，这里有参考文章 <https://ceph.com/planet/bring-persistent-storage-for-your-containers-with-krbd-on-kubernetes/> 。

如果想手动在容器中map一个RBD image，通过已有的命令就可以实现，运行容器时需要提前把`/dev`和`/sys`挂载到容器内，详细教程可参考Ceph committer的文章 <http://www.sebastien-han.fr/blog/2015/06/26/map-a-rbd-device-inside-a-docker-container/> 。而volume plugin只是通过API执行类似的操作，如果无须自动化也可以手动管理持久卷。

## 持久化容器

为了让容器后端使用持久化的分布式存储，可以参考这个文档使用修改过的Docker <http://hustcat.github.io/run-docker-on-ceph/> 。这个Patch是在这个PR上提的 <https://github.com/docker/docker/pull/14800> ，最后是希望通过这个PR的合并来实现 <https://github.com/docker/docker/pull/13777> ，目前Docker官方仍不支持直接使用RBD后端。

要实现持久化容器通过Kernel RBD直接mount到特定目录也是可以实现了，我们能直接修改创建容器的脚本，这里以LXC容器为例 <http://cephnotes.ksperis.com/blog/2014/11/17/ceph-rbd-with-lxc-containers> 。当然在Docker官方支持之前我们也不建议手动把容器rootfs挂载到RBD上。


## 推荐

最后忍不住推荐在容器和分布式存储都有深入研究的腾讯工程师和他的博客 <http://hustcat.github.io> 。