+++
date = "2016-01-09T09:42:18+08:00"
draft = true
title = "Spark DataFrame入门教程"

+++

## 介绍

DataFrame是Spark推荐的统一结构化数据接口，基于DataFrame快速实现结构化数据的分析，详细使用教程在https://spark.apache.org/docs/latest/sql-programming-guide.html

## 使用

创建SparkQL的上下文。

```
from pyspark.sqlimportSQLContext

sqlContext = SQLContext(sc)
```

导入JSON文件数据，DataFrame也支持从RDD、JDBC、Hive等数据源导入数据。

```
df = sqlContext.read.json("/tmp/git.json")
git.json的数据格式类似这样，可以通过git log --pretty=format:'{"commit":"%H","author":"%an","author_email":"%ae","date":"%ad"}' > git.json来生成。

{"commit":"fbbf4b22db7857f11018f0153472d909af874c31","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Fri Jan 1 09:47:31 2016 +0800"}

{"commit":"22ef72a98c9dfe2f63db9cf34c635124b2d61676","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Wed Dec 30 15:04:16 2015 +0800"}

{"commit":"1c6f4826526149d1df4d6f49c4cd54def5c09ec0","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Wed Dec 30 14:59:18 2015 +0800"}

{"commit":"56b4161ff9913033fe0dcdf291eca9ec0a6a9cc5","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Wed Dec 30 09:19:56 2015 +0800"}

{"commit":"0c8c9b065ad381362cbe6726df09b939796175ae","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Tue Dec 29 15:10:43 2015 +0800"}

{"commit":"b4e784bf78a83a922cff31de239c21b168bc7809","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Tue Dec 29 15:09:58 2015 +0800"}

{"commit":"2e02e17465c2594defb81c439bffe3a3a63ddf92","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Mon Dec 28 20:12:24 2015 +0800"}

{"commit":"185507c50f91a32172a106dd2d1b2fba5cab129c","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Sun Nov 29 22:47:18 2015 +0800"}

{"commit":"512761a255619d6dc81c4ba2d892d397b390b978","author":"tobe","author_email":"tobeg3oogle@gmail.com","date":"Sun Nov 29 21:59:29 2015 +0800"}
```

基本操作。

```
df.show()

df.printSchema()

df.select("author").show()

df.filter(df['author'] !="tobe").show()

df.groupBy("author").count().show()
```

执行SQL命令。

```
df.registerTempTable("git")

df = sqlContext.sql("SELECT * FROM git").show()
```

通过代码创建DataFrame。

```
anotherPeopleRDD = sc.parallelize(['{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}'])

anotherPeople = sqlContext.jsonRDD(anotherPeopleRDD)
```

准备MySQL数据库。

```
apt-get install -y libmysql-java

mysql -uroot -p

create database spark_db;

use spark_db;

create table spark_table (name varchar(20), ageint(32));

insert into spark_table values ("tobe",18);

insert into spark_table values ("john",28);
```

连接MySQL。

```
SPARK_CLASSPATH=/usr/share/java/mysql-connector-java.jar ./pyspark

from pyspark.sqlimportSQLContext

sqlContext = SQLContext(sc)

dataframe_mysql = sqlContext.read.format("jdbc").options(url="jdbc:mysql://127.0.0.1:3306/spark_db", driver="com.mysql.jdbc.Driver", dbtable="spark_table", user="root", password="root").load()

dataframe_mysql.show()
```