+++
date = "2016-01-10T08:35:33+08:00"
draft = true
title = "mount cloud disk"

+++



## Create the cloud disk

Create the disk and bind to the vm.

## List the block device

```
lsblk
```

## Format the device

```
mkfs.ext4 /dev/vdb
```

## Mount the disk

```
mount /dev/vdb /opt/stack/data/nova/instances/
```