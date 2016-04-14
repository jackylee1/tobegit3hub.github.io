+++
date = "2016-04-14T22:19:02+08:00"
draft = true
title = "基于Ansible实现自动化运维工具"

+++


## Ansible简介

Ansible是目前最火热的Devops工具之一，没有复杂的Master/Slave架构，通过简单的SSH协议实现了强大的功能。目前大家常用Ansible做配置管理，而且OpenStack社区基于Ansible加Docker来快速部署IaaS服务，甚至还有使用Ansible做性能测试和HA测试，同时做服务的健康性检查。

我之前写过博客 [ansible in five minutes](http://chendihao.cn/post/ansible-in-five-minutes/) 简单介绍了语法，Ansible就像分布式的Shell可以灵活实现自动化的工具，于是很早以前就有了 [osop](https://github.com/tobegit3hub/osop) 这个工具。

## 设计自动化运维工具

在IT领域，运维无非就是编写一些列脚本和命令，在本地执行或者远程执行、批量执行，这些Ansible都可以做到，而且实现方式比较“原生”，基本Shell该如何执行的，用Ansible也能轻易实现，这比相对复杂的Puppet无论是开发成本还是维护成本都会低很多。

例如我们会对服务器进行分组，这些分组都可以写到hosts文件中，以后可以批量或者随意执行命令，以下是一个Ansible hosts文件的例子。

```
[compute]
55.17.52.[1:30]

[api]
55.22.[56:57].105
55.22.56.106

[db]
55.22.[56:57].135
55.22.56.136
```

然后我们批量执行命令就非常简单了，例如对所有db节点执行mysqldump命令，或者是其他任意的命令。

```
ansible -i ./hosts db  -m command -a 'mysqldump'
```

批量拷贝文件也非常简单，例如我们要执行复杂的操作，可以先写到脚本中，然后拷贝批量执行。虽然Ansible批量执行很方便，但因为Ansible只能把标准输入、标准输出返回，因此中间的输出不能同步返回，因此我们也推荐使用更轻量的批量管理工具 [clushtershell](https://github.com/cea-hpc/clustershell) 。

```
ansible -i ./hosts db -m copy -a 'src=/Users/tobe/script.sh dest="/Users/tobe/script.sh"'
```

## OpenStack自动化运维工具

有了前面这么多铺垫，相信大家对Ansible能做到的程度有一定的了解，但是其实，在特定场景下我们甚至可以做到更极致。

在我们企业版OpenStack的环境中，日常的运维操作无非就是重启各种服务、测试Ceph集群可用性、测试能否创建虚拟机，由于涉及多节点操作而且不同服务重启方式不同，我们频繁在clush中重复操作了。于是我们有了 [osop](https://github.com/tobegit3hub/osop) 工具，先来看看 [演示视频](http://v.youku.com/v_show/id_XMTQ5MTIzMzQyMA==.html) 。

我们用Ansible Playbook实现了多种高可用服务，例如Nova、Cinder、Glance、Memcache、RabbitMQ、MariaDB等服务的重启操作，通过脚本实现Ansible自动化创建虚拟机和云硬盘，通过Playbook来简化Ceph集群状态的检测。最最最重要的是，我们基于ncurses实现了交互式界面，也就是说没有任何命令行使用经验的人都可以轻松玩耍ansible-playbook，而不会误用或者陷入实现的细节，大家看截图就知道。

![](https://raw.githubusercontent.com/tobegit3hub/osop/master/screenshot.png)

有了Ansible工具，我们不仅可以实现批量服务器的运维，可以对服务器进行分组管理，可以通过Playbook实现自动化操作，后续我们还可以加上测试和HA配置，事实上我们已经使用Ansible优化我们的部署流程。更多技术介绍也可以关注 [UnitedStack官方博客](https://www.ustack.com/about/blog/) ，讲了这么多大家才知道这是一篇广告博文 ^_^