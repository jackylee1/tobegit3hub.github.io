+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "introduce chronos zh"

+++



## 源码

https://github.com/XiaoMi/chronos.git

## 简介

Chronos，在古希腊语意为[时间](http://en.wikipedia.org/wiki/Chronos)，是实现**高可用**、**高性能**、**提供全局唯一而且严格单调递增timestamp**的服务。

Chronos采用主备架构，主服务器挂了以后备服务器迅速感知并接替服务，从而实现系统的高可用。服务端使用[Thrift](http://thrift.apache.org/)框架，经测试每秒可处理约60万次RPC请求，客户端单线程每秒可请求6万次(本地服务器)，保证高性能与低延时。全局只有唯一的ChronosServer提供服务，分配的timestamp保证严格单调递增，并且将已分配的值持久化到ZooKeeper上，即使发生failover也能保证服务的正确性。

## 原理

![chronos architecture](/uploads/default/16/479dd846d7b1fee1.png)

Chronos依赖[ZooKeeper](http://zookeeper.apache.org/)实现与[HBase](https://hbase.apache.org/)类似的Leader Election机制，ChronosServer启动时将自己的信息写到ZooKeeper的Master临时节点上，如果主服务器已经存在，那么就记录到BackupServers节点上。一旦Master临时节点消失(主服务器发生failover)，所有备服务器收到ZooKeeper通知后参与新一轮的选主，保证最终只有一个新的主服务器接替服务。

ChronosServer运行时会启动一个Thrift服务器，提供getTimestamp()和getTimestamps(int)接口，并且保证每次返回的timestamp都是严格单调递增的。返回的timestamp与现实时间有基本对应关系，为当前Unix time乘以2的18次方(足够使用1115年)，由于我们优化了性能，所以如果存在failover就**不能保证这种对应关系的可靠性**。

ChronosClient启动时，通过访问ZooKeeper获得当前的主ChronosServer地址，连接该服务器后就可以发送Thrift RPC请求了。一旦主服务器发生failover，客户端请求失败，它会自动到ZooKeeper获得新的主ChronosServer地址重新建立连接。

## 使用

### Chronos服务端

1. 进入chronos-server目录，通过`mvn clean package -DskipTests`编译源码。
2. 进入target里面的conf目录，编辑chronos.conf，填写依赖的ZooKeeper配置。
3. 进入target里面的bin目录，执行`sh ./chronos.sh`既可运行ChronosServer。

### Chronos客户端

1. 进入chronos-client目录，通过`mvn clean package -DskipTests`编译源码。
2. 客户端在pom.xml添加chronos-client的依赖(**请使用对应的Thrift版本**)。

     ```
     <dependency>
       <groupId>com.xiaomi.infra</groupId>
       <artifactId>chronos-client</artifactId>
       <version>1.2.0-thrift0.5.0</version>
     </dependency>
     ```

3. 创建ChronosClient对象，如`new ChronosClient("127.0.0.1:2181", "default-cluster")`。
4. 发送RPC请求，如`chronosClient.getTimestamp()`或`chronosClient.getTimestamps(10)`。

### 快速体验

1. 参考[ZooKeeper文档](http://zookeeper.apache.org/doc/trunk/zookeeperStarted.html)，编译ZooKeeper并运行在127.0.0.1:2181上。
2. 获得chronos源代码，执行`mvn clean packge -DskipTests`编译(需要安装Thrift)。
3. 进入chronos-server的bin目录，执行`sh ./chronos.sh`运行ChronosServer。
4. 进入chronos-client目录，执行`mvn exec:java -Dexec.mainClass="com.xiaomi.infra.chronos.client.ChronosClient" -Dexec.args="127.0.0.1:2181 default-cluster"`。

## 场景

* 提供全局严格单调递增的timestamp，用于实现[Percolator](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36726.pdf)等全局性事务。
* 提供全局唯一的值，相比[snowflake](https://github.com/twitter/snowflake)不依赖NTP服务，并且提供failover机制。

## 工具

* 提供list_servers.rb脚本，可监控当前的所有运行的ChronosServer状态。
* 提供translate_timestamp.rb脚本，可将timestamp转化为可读的世界时间。
* 提供process_benchmark_log.rb脚本，可处理Benchmark程序产生的日志。

## 测试

* 性能测试

| 客户端线程数 | 平均QPS | 平均Latency(毫秒) | 平均Failover时间(秒) | 服务端总QPS |
|