+++
date = "2016-01-10T08:35:30+08:00"
draft = true
title = "easy way to install java"

+++



1. sudo apt-get purge openjdk*
2. sudo add-apt-repository ppa:webupd8team/java
3. sudo apt-get update
4. sudo apt-get install oracle-java6-installer
5. set /usr/lib/jvm/java-6-oracle as $JAVA_HOME