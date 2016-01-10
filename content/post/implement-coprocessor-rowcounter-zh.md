+++
date = "2014-10-07T08:35:32+08:00"
draft = true
title = "implement coprocessor rowcounter zh"

+++



<img src="https://hbase.apache.org/images/hbase_logo.png">

### 概述
分布式数据库HBase本身不支持SQL语法，要统计表的行数，只能通过其他的方式来实现。HBase的shell脚本提供了count命令，但该命令只是简单地scan全表然后将行数累加，效率很低只能用于测试或者统计小表了。另一解决方案是使用MapReduce，HBase自身提供了org.apache.hadoop.hbase.mapreduce.RowCounter类，可以方便地在命令行调用进行统计，但执行效率仍难以达到我们的需求。HBase 0.92引入了Coprocessor这项特性，可以很方便地在RegionServer端实现各类聚集操作，通过AggregationClient#rowCount这个接口就可以相对高效地统计表的行数了。

### 实现
Coprocessor提供了Observer和Endpoint两项特性，前者允许通过重写函数在RegionServer端注入用户代码，后者则相当于数据库中的触发器(详细介绍参考[Reference1](http://blogs.apache.org/hbase/entry/coprocessor_introduction ))。社区依此为聚集操作提供了AggregateProtocol接口和AggregateImplement实现，我们使用AggregationClient就可以并发对每个region进行rowCount等操作，同时设置了FirstKeyOnlyFilter以提高执行效率，然后将结果返回client端进行累加，与直接scan全表相比极大提高了统计的并行度，配置HBase使用Coprocessor可以参考[Reference2](http://michaelmorello.blogspot.jp/2012/01/row-count-hbase-aggregation-example.html)。

当然，我们在实际统计过程中也遇到了不少的问题，首先就是跑Coprocessor消耗了太多系统资源。如果全速跑的话，每个region线程都可能把100%的CPU利用率耗完，当一台RegionServer有多个region时对其他服务的影响就更大了，这对在线业务可是不能接受的。我们的解决方案是选择在凌晨低峰期跑，而且优先选择离线集群和备集群，于是我们实现了CoprocessorRowcounter这样一个工具，在给定的时间内调用统计函数并将结果输出到本地或HBase数据库中，代码已经反馈到社区了（请参考[Reference3](https://issues.apache.org/jira/browse/HBASE-9800)）。但实际上如果不限制并行scan的region数和访问的qps，这个程序还是有可能把RegionServer跑垮，于是我们改进了AggregationClient的线程池，允许用户指定最大的并发数，同时加入对qps的限制，保证对服务端不会有过于频繁的访问。还有一个微小的改进，就是对划分出来的region key数组进行shuffle，然后将数组依次放入线程池中，这样尽可能保证了scan的压力可以均分到每台RegionServer上。开发时还发现rowCount必须指定colum family，于是找到相应的issue并backport到0.94(详见[Reference4](https://issues.apache.org/jira/browse/HBASE-9830))，问题解决同时反馈到社区了。

### 实践
CoprocessorRowcounter已经在实践中统计了我们大部分表的行数，正确性也经过了验证，存在的问题主要是资源占用率过高，不宜用于在线集群。其次效率仍需提高，即使能够对region进行并发操作，大表的统计仍需要分钟级甚至是小时级的耗时。实践也发现每次rpc调用时间都比正常操作长很多，所以务必将hbase.rpc.timeout设置为Integer.MAX_VALUE，才能保证程序不会因为rpc超时而退出。

### Reference
[1]Coprocessor Introduction http://blogs.apache.org/hbase/entry/coprocessor_introduction
[2]HBase Aggregation Example http://michaelmorello.blogspot.jp/2012/01/row-count-hbase-aggregation-example.html
[3]CoprocessorRowcounter Issue https://issues.apache.org/jira/browse/HBASE-9800
[4]Backport HBASE-9605 https://issues.apache.org/jira/browse/HBASE-9830
