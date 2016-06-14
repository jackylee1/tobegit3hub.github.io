+++
date = "2016-06-14T10:30:52+08:00"
draft = true
title = "Create Ubuntu Boot Udisk"

+++

## Tutorial

Download the Ubuntu image as iso file. Use `lsblk` to checkout the label of Udisk.

```
dd count=1 bs=512 if=/dev/zero of=/dev/sdb && sync
```

Make sure that you should rewrite the partition table, not rewriting /dev/sdb2 or others.