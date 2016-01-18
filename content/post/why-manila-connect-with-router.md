+++
date = "2016-01-01T09:38:24+08:00"
draft = true
title = "文件共享服务为什么要连路由器？"

+++

## 文件共享服务介绍

文件共享服务，就是在云上提供共享文件系统，让多台云主机非常方便地共享文件，最参见的共享文件系统包括NFS和CIFS。

为了实现文件共享服务，我们基于OpenStack Manila顶级项目提供了NFS和CIFS文件共享的支持。

## Manila项目介绍

Manila是IaaS上文件共享服务的工业标准，通过driver的方式实现多种存储后端，使用方法也很简单。

第一步，创建私有网络。

![](/images/create-private-network.jpg)

第二步，私有网络绑定路由器。

第三步，创建共享网络。

![](/images/create-share-network.jpg)

第四步，创建文件共享。

![](/images/create-file-share.jpg)

## Manila绑定路由器

基本步骤大家应该没什么疑惑，但第二步为何要将私有网络绑定路由器呢？带着这个疑问我们来看看Manila的架构。

从官方文档我们可以看到，地址是 http://docs.openstack.org/developer/manila/devref/generic_driver.html

```
Service VM has one net interface from net that is connected to public router. For successful creation of share, user network should be connected to public router too.

Service VM has two net interfaces, first one connected to service network, second one connected directly to user’s network.
```

而我们的share server是单网卡的，因此这里提示用户网络必须连接路由器。

看看我们网络组大牛分析的《Manila网络模块》你就能理解了，传送门 http://mytrix.me/2015/01/network-part-of-manila/

![](/images/manila-network-topology.jpg)


我们知道Manila创建的虚拟机share server是在Manila's Network中，而用户的虚拟机是在User's Network中，如果share-server只有一块网卡（port），只能通过User's Router来打通网络了。如果share-server有两块网卡（port），也可以直接连接用户私有网络，这也是官方文档表达的。

## 更多Manila教程

如果想了解更多Manila相关的服务和教程，欢迎使用UnitedStack(https://www.ustack.com/)的文件共享服务和关注我们的博客。
