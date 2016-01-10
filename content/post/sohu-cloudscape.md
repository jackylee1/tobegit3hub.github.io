+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "sohu cloudscape"

+++



## 云景简介

云景是搜狐的PaaS平台，服务了内部上百个应用，现在已经对外发布了。

云景服务器基于Linux 2.8左右的内核，合并了Upstream一些Patch和做了改进。最开始是基于Java的沙盒技术，为了支持更多的语言使用LXC，现在的架构是LXC+MQ+OVS。

未来会支持Docker应用，和Azure合作未来提供Windows虚拟机。

## 实践遇到的问题

* 要监控容器内进程是否异常退出，LXC只支持Container的监控。
* 容器的网络流量控制，最后好像是用tc来实现的。
* Proc文件系统的隔离，以前内核不支持所以容器内top会显示宿主机的进程，而且直接访问/proc/sysrq-trigger可以让宿主机重启。目前Docker也已经解决这个问题了。
* 容器和宿主机共享同一个Cgroups带来一些问题。
* Setns问题，可能是线程脱离容器的命令空间还是什么。
* 支持OverlayFS。这和Docker使用的AUFS类似。
* 支持Netoops，这可以把容器崩溃的信息收集到远端。

## 云景提供的服务

* 通过冗余来实现高可用，建议用于一个应用起多个容器，否则一个容器升级时会不可用。
* 利用规则引擎，可以动态调整实例。
* 用户可以通过git、console、web来提交代码，最终都会用git存，除了像Java这种编译型语言。
* 应用需要写一个app.yaml，代码放在app目录，Python依赖使用requirements.txt，Ruby用Gemfile，Node用package.json。
* 他们容器可能挂的，所以要求用户的应用都是无状态，如果需要状态可以使用Cache或者存储服务。
* 提供粘性会话功能，也就是可以让一个用户始终访问App的某一个容器。
* PaaS平台会监控容器的QPS、响应时间还有容器性能。
* 他们提供一套日志系统，收集access、app、stdout日志，分析系统包括FlumeNg、Spark、Storm。
* 提供二级域名，允许绑定已备案的域名，他们也提供备案服务。
* 用户可以SSH到容器，需要手动开启，而且上去只读。
* 提供Cache（Memcache支持多租户，Redis只有主从），文件存储服务，MySQL（开源了一个proxy项目，提供phpadmin接口），没有MQ服务。
* MySQL开源的proxy项目可以实现acl、黑白名单、限制危险操作。
* 使用Cgroups动态修改容器配置，不需要重启容器。

