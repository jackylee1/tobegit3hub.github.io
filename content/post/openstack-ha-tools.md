+++
date = "2016-01-11T10:33:22+08:00"
draft = true
title = "openstack ha tools"

+++


## Pacemaker

pacemaker作用是支持按顺序启动（libvirt比nova前），多活但不能同时起（rabbitmq按顺序加），比systemd更强的状态服务状态检查，让cinder-volume本地重启不行则迁移。

客户端通过hostname或vip来实现高可用，如果使用hostname找DNS会有超时时间，希望是主被模式所以使用vip。

API节点没有用vip，是连任意一个Haproxy，具体要看Haproxy配置，可以获取多个IP来RoundRobin。Haproxy可以起多个，类似galera，但是通过vip访问因此只有一个主。

API三个节点组成一个pacemaker集群，实现多活。LBS组成一个pacemaker集群实现vip的主从。

cinder-volume、vip都是一个pacemaker资源，一个集群内多个资源可以有依赖关系。

几种模式，vip加多节点就是主被，vip加haproxy加多节点就是多活，cinder-volume就是当节点的冷备，通过rabbitmq的多节点多活。

## Haproxy

haproxy就做4层和7层负载均衡，还能做health check，这nginx不能做。目前memcache走四层，所有API都是HTTP七层。



