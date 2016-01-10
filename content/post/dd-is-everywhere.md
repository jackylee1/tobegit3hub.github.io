+++
date = "2013-09-14T08:35:30+08:00"
draft = true
title = "dd is everywhere"

+++



## Usage

* if for input file
* of for output file
* bs for block size and usually less than 512
* count for count and can be 1G
* /dev/zero for null for zero stream
* /dev/null for black hole

## Simulate disk full

* dd if=/dev/zero of=/dev/sdb bs=512 count=1G

## Simulate disk failure

* dd if=/dev/opt of=/opt_header bs=4098 count=1
* dd if=/dev/zero of=/dev/opt bs=4098 count=1
* umount and mount
* dd if=/opt_header if=/dev/opt bs=4098 count=1

## Backup

* dd if=/dev/sda of=/dev/sdb
