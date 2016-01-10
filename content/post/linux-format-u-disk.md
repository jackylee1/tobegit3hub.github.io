+++
date = "2013-01-11T08:35:28+08:00"
draft = true
title = "linux format u disk"

+++



需要mkfs.vfat工具，Ubuntu自带，archlinux请这样sudo pacman -S dosfstools

1. 查找U盘分区，`sudo fdisk -l`
2. 卸载，`umount /dev/sdb1`
3. `mkfs.vfat /dev/sdb1`