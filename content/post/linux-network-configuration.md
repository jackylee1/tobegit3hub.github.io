+++
date = "2013-01-05T08:35:27+08:00"
draft = true
title = "linux network configuration"

+++



## 两种配置方法：

1.启动dhcpcd自动分配IP（适用宽带）

2.手动配置静态IP（适用校园网）

2.1.设置DNS，cp /etc/resolv.conf.bak /etc/resolv.conf

2.2.设置IP，ip addr add 110.64.91.18/24 dev eth0，（可以多个重复，所以可能要del）

2.3.设置网关，ip route add default via 110.64.91.254

 
## 备注：

`pkill dhcpcd`

`ifconfig eth0 up`