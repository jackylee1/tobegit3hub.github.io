+++
date = "2014-08-20T08:35:31+08:00"
draft = true
title = "verify data between databases"

+++



In production environment, we always have a backup cluster for each database. If it's MySQL, we can use [pt-table-checksum](http://www.percona.com/doc/percona-toolkit/2.2/pt-table-checksum.html) to verify data. But if you migrate the data from MySQL to HBase, there's no tool to validate it.

Because of the complexity of schema between MySQL and HBase, we can't implement a general tool to validate data between any database. But for a specific case, I have the following solutions.

We can periodically `select` some records from MySQL and `get` from HBase, then compare the values of them. It's a underlying level and we just focus on the data itself.

We can also `select` some records to create the business objects. Then `get` the same one from HBase and compare these objects. It's a little high level and related to the business. But you can verify for a whole table for each comparison.

It would be great if you have a general method to do that.