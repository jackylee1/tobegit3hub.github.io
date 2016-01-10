+++
date = "2013-06-02T08:35:29+08:00"
draft = true
title = "setup windows 8 and fix grub"

+++



1. insert Ubuntu setup disk
2. `sudo -i` to login as root
3. `fdisk -l` to check linux partition
4. `mount /dev/sda5 /mnt` to mount
5. `grub-install –root-directory=/mnt /dev/sda` then print “Installation finished”
6. `umount /dev/sda5` to umount
7. reboot

