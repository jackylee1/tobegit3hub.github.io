+++
date = "2015-12-20T09:34:15+08:00"
draft = true
title = "Cinder创建卷流程分析"

+++

1.

创建卷可以通过命令发送请求，例如cinder create 1

2.

由cinder-api处理，代码在/cinder/cmd/cinder-api，这是标准的OpenStack Web应用，会读api-paste.ini并且传osapi_volume参数

3.

api-paste在正常请求会走v2api，最终定位到cinder.api.v2.router:APIRouter.factory

4.

这个router会响应volume的创建行为，使用/cinder/api/v2/volumes.py的VolumeController的create()

5.

首先是检查一下volume type，获取metadata、snapshot等参数进行检查，然后调用volume_api

6.

volume_api是读配置项volume_api_class，一般就是cinder.volume.api.API，然后使用flow_engine来创建

7.

这会调用/cinder/volume/flows/api/create_volume.py，检查quota之类的，并且创建VolumeCastTask

8.

接着是需要调用scheduler_rpcapi交给scheduler处理了，而这个函数是早在/cinder/volume/api.py的时候创建的，代码在/cinder/scheduler/rpcapi.py

9.

这只是scheduler的客户端，通过mq异步调用一个名为create_volume的函数

10.

cinder-scheduler是一个标准的OpenStack wsgi应用，监听mq，因此我们只要在/cinder/scheduler/manager.py找到create_volume函数即可

11.

scheduler则是使用自己的flow类来创建volume，这是它传入了driver类，这是同配置项scheduler_driver指定的，一般是cinder.scheduler.simple.SimpleScheduler

12.

实际上通过/cinder/scheduler/manager.py的代码可以看到，使用cinder.scheduler.chance.ChanceScheduler或cinder.scheduler.simple.SimpleScheduler最后都会用cinder.scheduler.filter_scheduler.FilterScheduler

13.

然后我们在/cinder/scheduler/filter_scheduler.py看到schedule_create_volume()，首先更新下数据库，然后调用/cinder/volume/rpcapi.py的create_volume()，也就是通过mq请求create_volume()

14.

这个消息回由cinder-volume的manager来处理，这个方法也是使用flow（注意与前面api和scheduler用的不是同一个文件），其中最重要的是执行CreateVolumeFromSpecTask这个任务

15.

直接看/cinder/volume/flows/manager/create_volume.py的execute()，其中它要调一个driver，这是同配置项volume_driver指定的，我们是用cinder.volume.drivers.rbd.RBDDriver

16.

然后根据传入的类型，例如raw，直接调用create_functor()，这会调用内部函数_create_raw_volume()，使用driver的create_volume()

17.

最后我们也是调用rbd的python library来创建卷

