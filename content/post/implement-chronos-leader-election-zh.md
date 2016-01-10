+++
date = "2014-10-16T08:35:32+08:00"
draft = true
title = "implement chronos leader election zh"

+++



## 开源地址
<https://github.com/Xiaomi/chronos>

## 选主模块
* Chronos-server依赖ZooKeeper来选主。
* 实现机制与HBase的HMaster一样，对master节点进行watch。
* 主要逻辑在FailoverServer.java和FailoverWatcher.java。

<https://github.com/XiaoMi/chronos/blob/master/chronos-server/src/main/java/com/xiaomi/infra/chronos/zookeeper/FailoverWatcher.java>

## 源码分析
* `hasActiveServer`表示当前Cluster的状态。
* `process`用于监听和处理所有ZooKeeper实践。
* 一旦有znode变化，调用`handleMasterNodeChange`来通知对象。
* 抢主和等待的逻辑在`blockUntilActive`来处理。
