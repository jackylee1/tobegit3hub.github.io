+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "note of mongodb"

+++



* the basic unit of MongoDB is document
* you can use JavaScript Shell to manager it
* all the document have the unique key, “_id”
* document consists of key-value pairs which are in order(like dictionary in Python)
* collection is a group of documents just like table
* the index is defined by the collection
* data is in /data/db and port number is 27017
* just “mkdir -p /data/db”
* “sudo mongod” to run
* “sudo mongo” to its shell which runs all JavaScript
* automatively connect with database test and named as db
* the type of _id is ObjectId rather than auto increasing int, 12 Bytes
* time stamp, machine number, PID, counter
* MongoDB developer chooses unsafe as default
* Ruby, Python and Java drivers use connection pool for performance
* MongoDB uses PCRE, which is compacity with Perl
* $where is not good
* use the last date rather than skip() for paging
* index here is exactly as same as relational database
* MapReduce is the star of counting
* pymongo.connection()