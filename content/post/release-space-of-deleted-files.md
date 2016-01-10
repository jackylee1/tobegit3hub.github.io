+++
date = "2016-01-10T08:35:30+08:00"
draft = true
title = "release space of deleted files"

+++



## Check free space

`df -h`

## Check disk use

`du . –max-depth=1 -h`

## Check opened file

`lsof |grep “delete”`

## Check process

`ps aux |grep $pid`

## Kill it

`kill $pid or kill -9 $pid`