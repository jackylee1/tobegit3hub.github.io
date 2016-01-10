+++
date = "2013-01-04T08:35:27+08:00"
draft = true
title = "arch i love u"

+++



第一次安装Arch Linux，果然很DIY，看看安装步骤吧：-0

1. 下载刻录archlinux-dual.iso
2. loadkeys uk，设置键盘，可跳过
3. 提前gparted分区格式化，ext4即可
4. mount /dev/sda6 /mnt，挂载硬盘
5. dhcpcd，或者静态IP
6. /etc/pacman.d/mirrorlist，将China源提前
7. pacstrap /mnt base base-devel，下载基本包，很慢哦
8. arch-chroot /mnt pacman -S grub-bios，安装grub
9. genfstab -p /mnt >> /mnt/etc/fstab，写入文件系统信息，很重要
10. arch-chroot /mnt，进去
11. ln -s /usr/share/ zoneinfo/Asia/HongKong /etc/localtime
12. mkinitcpio -p linux，与RAM有关
13. passwd，设root密码
14. exit，出来
15. umount /mnt/{boot,home,}，卸载
16. /etc/pacman.conf，貌似x64的设置没用
17. reboot