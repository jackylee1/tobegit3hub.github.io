+++
date = "2016-02-18T18:03:19+08:00"
draft = true
title = "implement failover framework reference"

+++

## 参考项目

最经典的是Netflit的ChaosMonkey项目，是Java实现的，还带failover的故障模拟脚本，项目地址 <https://github.com/Netflix/SimianArmy> 。

当时我在小米实现了针对Hadoop和HBase的failover测试框架，项目地址（私有Repo） <https://github.com/tobegit3hub/infra_github/tree/master/machine-failover> ，代码不是开源的但可以看当时的设计文档，也是我的本科毕业paper <https://github.com/tobegit3hub/failover_paper> 。

准备贡献到社区的Jira讨论，地址是 <https://issues.apache.org/jira/browse/HBASE-9802> 。

## 未来考虑

未来我们将用Python重新设计failover测试框架，可以针对Docker、OpenStack等分布式项目，项目地址是 <https://github.com/tobegit3hub/failoverd> 。