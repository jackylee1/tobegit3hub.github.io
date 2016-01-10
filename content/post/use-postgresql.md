+++
date = "2016-01-10T08:35:31+08:00"
draft = true
title = "use postgresql"

+++



## Command

* `su - postgres`
* `psql $table_name`
* `createuser -s -r tobe` to create new role
* `\q` to quit

## Ruby Code

<pre>
require 'pg'
connection = PGconn.open(:dbname => :test_db, :password => :postgres)
result  = connection.exec("select * from test_tabel")
result[0] # {"name"=>"tobe"}
</pre>

## Reference
* <http://www.yiibai.com/html/postgresql/2013/080333.html>
* <http://www.pgsqldb.org/pgsqldoc-8.1c/tutorial.html>
* <http://stackoverflow.com/questions/4683057/simple-example-of-postgres-query-in-ruby>
