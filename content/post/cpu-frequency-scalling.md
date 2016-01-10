+++
date = "2013-12-24T08:35:30+08:00"
draft = true
title = "cpu frequency scalling"

+++



## Cpu Frequency Scalling

* <http://en.wikipedia.org/wiki/Dynamic_frequency_scaling>
* <https://wiki.archlinux.org/index.php/CPU_Frequency_Scaling>
* <https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Power_Management_Guide/cpufreq_governors.html>
* <https://www.kernel.org/doc/Documentation/cpu-freq/governors.txt>

## Linux

* list module, lsmod grep cpufreq
* know about cpu frequence governor, <https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Power_Management_Guide/cpufreq_governors.html>
* refer https://wiki.archlinux.org/index.php/CPU_Frequency_Scaling
* use cpufreq-set and refer <http://www.thinkwiki.org/wiki/How_to_use_cpufrequtils>
* current cpu frequency, cat /proc/cpuinfo
* find the max value, dmidecode -t processor |grep “Speed”
* more command refer <http://askubuntu.com/questions/218567/any-way-to-check-the-clock-speed-of-my-processor>

## Ubuntu

* refer http://www.pantz.org/software/cpufreq/usingcpufreqonlinux.html
* list all policy, sudo cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors
* current policy, sudo cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
* set policy, sudo sh -c “echo ondemand > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor”
* the default value of oncommand, sudo cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
* show policy and all info, sudo apt-get install cpufrequtils then cpufreq-info

## CentOS

* list all policy, ls /lib/modules/$(uname -r)/kernel/drivers/cpufreq
* refer http://murty4all.blogspot.jp/2010/11/changing-cpu-frequency-scaling-governor.html
* check policy, cat /etc/sysconfig/cpuspeed
* set policy, service cpuspeed restart
* show policy and all info, yum install cpuspeed cpufrequtils then cpufreq-info