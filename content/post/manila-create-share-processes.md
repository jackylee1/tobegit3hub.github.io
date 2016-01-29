+++
date = "2015-12-28T09:30:49+08:00"
draft = true
title = "Manila创建share流程分析"

+++

1.

要创建share，可以直接在命令行执行这个manila create nfs 10 --name $share1 --share-network-id $share-network-id

2.

接受请求的是manila-api进程，它的入口在/bin/manila-api.py，启动一个api-paste应用，并且指定的配置是osapi_share

3.

看api-paste.ini的osapi_share，正常逻辑走v1接口，会直接起manila.api.v1.router:APIRouter.factory

4.

这就是标准的OpenStack wsgi应用了，可以直接看/manila/v1/router.py看一下具体的路由

5.

share和shares的API都会用/manila/shares.py的ShareController，如果是POST请求就调action函数，最终会调create（代码没有找到原因？）

6.

/manila/shares.py的ShareController.create()实现了创建的逻辑，从body中获取size、proto（协议）等，如果有snapshot_id就检查一下保证share_network一致

7.

然后调用share_api.create()，这个share_api是通过配置文件的配置项share_api_class指定的，一般就只有一个manila.share.api.API

8.

API的create()先检查如果使用snapshot时的限制，还检查和预分配quota，然后直接把manila instance写到数据库

9.

然后是通过scheduler_rpcapi.create_share()异步创建share的nova instance和cinder instance

10.

scheduler的代码在/manila/scheduler/rpcapi.py，然后给mq发创建share的消息，注意这里是scheduler的客户端也就是还在manila-api进程内调用

11.

scheduler也是标准的OpenStack service应用，监听mq发送了函数名为create_share的请求，然后调用driver的函数，这个driver是通过配置项scheduler_driver指定的，一般就是manila.scheduler.filter_scheduler.FilterScheduler

12.

这个scheduler就是执行下filter操作，返回符合条件的host列表，把host等参数传进去又调share的rpc请求，这时候可以指定那台host来接受消息

13.

往mq发函数名create_share后，应该由manila-share来除了，这也是标准的OpenStack service，只监听mq，不对外提供API

14.

首先是/manila/share/manager.py的create_share响应这个消息，它在初始化是会读配置项share_driver，我们使用的是nova加cinder的generic driver

15.

这里判断如果给了snapshot_id就查他的parent_share_server_id，否这就调一下_provide_share_server_for_share()来创建或复用share server

16.

选择driver后在/manila/share/drivers/generic.py，会直接创建volume、attach上去、格式化、mount上去

17.

在attach的时候会调compute_api，这个是从配置项compute_api_class读出来的，一般都是manila.compute.nova.API，这里是外面传入nova instance直接attach的

18.

具体在那一台nova instance挂volumn是在传入参数share_server['backend_details']['instance_id']指定的，原来generic有个变量service_instance_manager可以管理nova instance和网络。