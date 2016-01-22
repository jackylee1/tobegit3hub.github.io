+++
date = "2015-12-19T09:25:12+08:00"
draft = true
title = "State of art technology DBaaS"

+++

## DBaaS简介

State of the art，中文可以译为“最先进的”，DBaaS也就是数据库服务。与单机版MySQL或者集群版Oracle不同，DBaaS将数据库作为服务来交付，任何人都可以轻易地创建、使用、扩容和销毁数据库实例，由基础平台负责监控和运维，开发者可以做到只关心业务而屏蔽底层细节。

![](/images/dbaas.jpg)

作为行业标准的MySQL，提供了高性能、易部署的数据库服务，但并没有解决多租户以及运维方面的问题。实际上大部分互联网公司的DBA，也是在做重复的运维工作，于是有两类公司开始思索做出改变，一是阿里这种内部大量使用数据库的亟需一种易运维、可控的DBaaS平台，另一类公司就是AWS、QingCloud这样的基础服务提供商。

![](/images/rds.jpg)

那UnitedStack这样的公司需要DBaaS吗？当然是需要的，我们在OpenStack社区逐渐看到UnitedStack对Trove项目的贡献（金山云却鲜有贡献）。Trove原意是宝藏，是目前仅有的开源DBaaS系统，如果你对数据库服务感兴趣不妨继续阅读下去。

## Trove项目介绍

Trove是OpenStack核心组件中的Database as a Service服务，它的Mission是让公有云/私有云用户可以轻易地部署Scalable和Reliable的数据库实例，并且提供一键创建、定期删除、快速扩容、自动备份、监控报警等功能。

![](/images/trove.jpg)

其实Trove项目早在2013年就启动，至今超过2000个commit和100百多个contributor，已经是OpenStack的顶级项目，而目前是否足够成熟呢？至少国外有一家数据库公司Tesora所有业务都是基于OpenStack Trove，并且国内XX云、XXStack也在积极将Trove部署到Production环境。Trove究竟有什么好呢，难道不能自己实现一套DBaaS吗？我们继续一探究竟。

## Trove架构分析

作为一款开源的DBaaS产品，对主流的MySQL支持显然是必须的，而令人惊喜的是，Trove不仅支持关系型数据库也支持非关系型数据（NoSQL）。从社区的Roadmap中看出对PostgreSQL、Redis、MongoDB、Cassandra、CouchBase、DB2的支持也在规划中，这得益于它API/Taskmanager/Conductor/Guestagent的良好架构。

![](/images/trove-architecture.jpg)

很多人会问，Trove的多租户是如何实现的呢？Keystone。Trove的网络是如何打通的呢？Neutron。Trove的数据库如何保证安全隔离的呢？通过Nova调度的虚拟机。因此，Trove项目实际上利用了OpenStack平台提供的服务，专注于DBaaS的架构，为云平台用户提供易用、免运维的数据库服务。

![](/images/trove-horizon.jpg)

那么Trove是如何实现同时对MySQL与Redis等“数据库”的支持呢？答案在于其架构中的Guestagent，与其他OpenStack项目一样，Trove通过API暴露RESTful接口、具体逻辑由Taskmanager处理，并且通过Conductor处理所有与本地数据库相关的操作，这些都为用户提供了一套统一的接口。而不同数据库的操作命令是不同的，因此我们需要为多个数据库类型实现多个Guestagent，它们接受Trove统一的命令并对底层数据库实例做不同的交互，Guestagent是直接整合到操作系统镜像中，可以伴随虚拟机快速启动。

## 这就是DBaaS

有人认为阿里的DBaaS就不是通过虚拟机实现的，不得不承认阿里在数据库运维上的积累，并且有能力修改源码提供安全的多租户环境。但Trove借助已经开源的计算、网络、存储以及认证等组件，通过虚拟机实现安全的隔离，提供原生的MySQL服务，并且实现了自动化维护的增、删、扩、备等功能，确实值得各位数据库开发者与DBA借鉴和学习。

![](/images/trove-cartoon.jpg)

作者本人专注于存储服务的开发与运维，目前为Trove社区提供了对Redis服务的支持（包括启停单个实例、配置组以及Replication集群等功能），欢迎与各位交流 https://github.com/tobegit3hub