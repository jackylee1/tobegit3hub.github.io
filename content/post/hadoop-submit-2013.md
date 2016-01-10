+++
date = "2016-01-10T08:35:30+08:00"
draft = true
title = "hadoop submit 2013"

+++



## Cassandra

* use cassandra replace redis
* cassandra transation to solve race condition
* consistent hash
* redudence for read
* hbase failover final consistency to read
* framework to test transation

## Drill

* drill and impala
* directly read hfile and memstore
* join for hbase and mysql

## HBase

* reduce to 5m to flush
* circuit read to skip datanode
* use queue for new write model
* zkquorm use dns circle query to get five ip

## Document Database
* mysql can partition but ask for partitionId
* mongodb impl secondary index
* hive and hdfs for etl
* telecon wants sql

## Redshift

* kafka to collect log
* offline analyse a/b test
* hive is high latency
* redshift as datawarehouse
* pinterest is driven by user decision
* posgress optimise data with current statistics
* worth doing by yourself
* monitor for shared service