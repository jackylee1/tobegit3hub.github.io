+++
date = "2016-04-15T11:15:35+08:00"
draft = true
title = "Pacemaker高可用方案初体验"

+++

## Pacemaker简介

虽然这不是最经典的Linux高可用教程，但通过此文档你可以快速精通Pacemaker、Corosync等技术，从而实现基于Linux的服务高可用配置。

高可用是应用开发者追求的特性，及时硬件故障、服务器宕机也能自动恢复服务，不需要人工接入。Google在设计分布式的Chubby、GFS和BigTable也就考虑到这点，而传统的Linux基础服务例如MySQL、RabbitMQ等原始为单机设计，在高可用上需要配合集群管理工具Pacemaker等才能实现，而且Corosync实现的类Paxos协议能容忍网络分区、节点故障等分布式问题。

## 动手配置Pacemkaer

Pacemaker依赖Corosync实现传输层的Quorum算法，一般配置奇数个选举节点，实现少数服从多数的策略，首先我们需要在节点安装对应的包。

```
yum install -y pacemaker pcs psmisc policycoreutils-python

systemctl start pcsd.service
systemctl enable pcsd.service
systemctl start corosync.service
systemctl start pacemaker.service

pcs cluster start --all
```

然后是配置节点间免秘钥登录，和配置Pacemaker集群，例如实验时我们是两节点。

```
ssh-keygen -t dsa -N ""
cp ~/.ssh/id_dsa.pub ~/.ssh/authorized_keys
scp -r ~/.ssh/ root@192.168.0.2:/root/

echo hacluster | passwd hacluster --stdin
pcs cluster auth 192.168.0.5 192.168.0.2
pcs cluster setup --name vip_cluster 192.168.0.5 192.168.0.2
```

接下来我们配置一个高可用的VIP资源，使用系统自带的ocf脚本。

```
pcs resource create p_vip ocf:heartbeat:IPaddr2 ip=192.168.0.200 cidr_netmask=24 op monitor interval=2s
pcs status

corosync-cfgtool -s

corosync-cmapctl |grep 'members'

crm_verify -L -V
```

这时大家可能发现有问题了，p_vip这个资源还是stopped状态，而且用crm_verify命令报错了，原因是系统默认开启了stonith功能，这是可以通过IPMI进行物理机关机的功能，可以更好地实现服务在网络分区时的高可用，由于我们暂时用不上所以先停了，所有资源也能正常起来。

```
pcs property set stonith-enabled=false
crm_verify -L
pcs status
```

## 高可用资源介绍

我们可以通过命令查看可选的资源格式。

```
[root@ha-test-1 ~]# pcs resource standards
ocf
lsb
service
systemd
stonith
```

也可以查看资源的实现provider，目前对OpenStack支持相当不错。

```
[root@ha-test-1 ~]# pcs resource providers
heartbeat
openstack
pacemaker
```

最后也可以看看ocf和heartbeat下有哪些资源可以直接使用的，包括前面已经用到的IPaddr2。

```
[root@ha-test-1 ~]# pcs resource agents ocf:heartbeat
CTDB
Delay
Dummy
Filesystem
IPaddr
IPaddr2
IPsrcaddr
LVM
MailTo
Route
SendArp
Squid
VirtualDomain
Xinetd
apache
clvm
conntrackd
db2
dhcpd
docker
ethmonitor
exportfs
galera
iSCSILogicalUnit
iSCSITarget
iface-vlan
mysql
named
nfsnotify
nfsserver
nginx
oracle
oralsnr
pgsql
postfix
rabbitmq-cluster
redis
rsyncd
slapd
symlink
tomcat
```

## 手动触发Failover

如果我们想测试这个节点挂了，可以手动移除节点模拟Failover，这时需要查看配置文件节点的标识。

```
pcs status

vim /etc/corosync/corosync.conf

pcs cluster stop 192.168.0.5
```

## 修改资源属性

我们也可以修改资源的默认属性。

```
pcs resource defaults resource-stickness=100
pcs resource defaults
```

或者修改某个资源特有的属性。

```
pcs resource show p_vip
pcs resource update p_vip monitor interval=3 timeout=20
pcs resource show p_vip
``

修改每个资源其他属性。

```
pcs resource meta openstack-cinder-volume migration-threshold=3 failure-timeout=60s

pcs resource meta ClusterIP resource-stickiness=0
```

## 添加依赖关系

Pacemaker支持资源间有依赖关系，可以添加新的p_vip2资源，然后保证他们在同一台服务器启动，而且可以设置启动顺序。

```
pcs resource create p_vip2 ocf:heartbeat:IPaddr2 ip=192.168.0.201 cidr_netmask=24 op monitor interval=2s

pcs constraint
pcs constraint colocation add p_vip with p_vip2 INFINITY

pcs constraint order p_vip then p_vip2

pcs constraint location p_vip prefers 192.168.0.2=100
```

然后检查score，判断资源会落到哪些服务器上。

```
crm_simulate -sL

pcs constraint --full
```

## STONITH

STONITH全称是Shoot The Other Node In The Head，也就是可以对其他节点进行关机操作，这在特定场合非常有用。例如我们有一个Active/Passive的单活资源，只能在一台服务器启动，如果Pacemaker的多个节点发生网络分区，那么Pacemaker有可能在两个节点同时启动这个服务，这时候如果开启STONITH功能就能对故障节点进行关机，保证服务高可用而且正确执行。

配置方法也很简单，不过注意需要物理服务器开启IPMI功能并且网络互通。

```
pcs stonith list

pcs stonith describe fence_ipmilan

pcs cluster cib stonith_cfg

pcs -f stonith_cfg stonith

#pcs -f stonith_cfg stonith create ipmi-fencing fence_ipmilan pcmk_host_list="pcmk-1 pcmk-2" ipaddr=10.0.0.1 login=testuser passwd=acd123 op monitor interval=60s
pcs stonith create server-69 fence_ipmilan pcmk_host_list="server-69" ipaddr=10.0.108.120 login=root passwd=calvin lanplus=1 cipher=1 op monitor interval=60s

pcs -f stonith_cfg property set stonith-enabled=true
pcs -f stonith_cfg property
```

最后我们可以测试STONITH，并且模拟重启操作。

```
pcs cluster stop pcmk-2
stonith_admin --reboot pcmk-2
```

## 参考文档

* 推荐[官方文档](http://clusterlabs.org/doc/en-US/Pacemaker/1.1-pcs/html-single/Clusters_from_Scratch/index.html)
