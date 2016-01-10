+++
date = "2015-02-28T08:35:32+08:00"
draft = true
title = "backup log"

+++



```
#!/bin/bash

if [ "$HOSTNAME" == "lg-xq-zn-udp00.bj" ];then

  d=`date -d"30 days ago" +%Y%m%d`
    if [ $# -gt 0 ];then
      yestoday=`date -d"$1 days ago" +%Y%m%d`
    else
      yestoday=`date -d"1 days ago" +%Y%m%d`
  fi

  mysqll -ufoo -pbar -h127.0.0.1 --default-character-set=utf8 db -N -e "select distinct uid from table where uid != 0" > /home/work/data/foo.log

  hadoop fs -mkdir /user/h_miot/airpurifier_users/$yestoday
  hadoop fs -put /home/work/data/airpurifier_users.log /user/h_miot/airpurifier_users/$yestoday/

  rm /home/work/data/airpurifier_users.log
  
fi
```