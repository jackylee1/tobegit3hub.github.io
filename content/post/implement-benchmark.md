+++
date = "2013-11-23T08:35:30+08:00"
draft = true
title = "implement benchmark"

+++



## Metrics

* qps( count/run_time)
* lantency

## Implement

* use ActomicInteger.incrementAndGet()
* new a thread to log the data
* add all latency and get the average
* you can record the max and min values

## Reference

* <http://code.google.com/p/thrift-rpc-benchmark/source/browse/src/main/java/com/googlecode/thriftbenchmark/rpc/BenmarkClient.java>
* <http://code.google.com/p/nfs-rpc/wiki/HowToRunBenchmark>
* <https://github.com/brianfrankcooper/YCSB>