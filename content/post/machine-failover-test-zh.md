+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "machine failover test zh"

+++



在进行Failover测试中，我们需要用软件模拟出CPU、内存、磁盘与网络等硬件的故障，这里总结一下所用到的工具与技术。

### RestartHost
>可以通过硬件控制卡强制重启机器，从而达到模拟宕机与重启操作系统的效果。如果权限允许也可以直接发reboot命令

### CpuLimit
> 要限制单个进程的CPU使用率，可以使用开源工具[cpulimit](https://github.com/opsengine/cpulimit)，我们需要在测试服务器上安装cpulimit，然后通过pid或者进程名对进程进行限制，如cpulimit -p 10086 -l 50即可限制pid为10086的进程CPU使用率不能超过50%，这里有一篇简易的[使用教程](http://www.cyberciti.biz/faq/cpu-usage-limiter-for-linux/)。如果想模拟机器CPU紧张的情景，也可以使用openssl工具，Netflix提供的[脚本](https://github.com/Netflix/SimianArmy/blob/master/src/main/resources/scripts/burncpu.sh)就是通过使用openssl speed来耗尽服务器的CPU，这样做的好处是真实地模拟了我们的测试场景，弊端就是会影响其他进程的执行。

### MemoryLimit
> 要模拟出内存受限的情景，我们参考前面限制CPU的方法，通过执行自己实现的内存消耗程序使被测进程的可用内存减少。我们找到一篇相当简单的[文章](http://minuteware.net/simulating-high-memory-usage-in-linux/)介绍实现一个内存消耗器，通过改造这个程序使我们可以随意启停对内存限制的模拟。要实现这个内存限制需要我们在服务器上手动编译这个C程序，生成对应的可执行程序。

### DiskFail
> 模拟磁盘故障的方式有很多，通过使用[fiu-ctrl](http://blitiri.com.ar/p/libfiu/doc/man-fiu-ctrl.html)可以很好地控制进程IO访问的失败率，继续了解发现libfiu的另一个优势在于不用注入代码，只是被测程序需要使用fiu-run来运行，小型程序可以很方便地控制各种IO读或写的成功率，但对于大型应用所有进程的启动入口都需要进行相应的修改。对于数据库系统，通过[删除数据库持久化文件](http://www.dba-oracle.com/t_simulating_server_disk_failures.htm)也能使大量磁盘请求失败，但也磁盘故障不能读写的情况还是有所区别。对于RAID磁盘阵列有相应的工具[mdadm](http://avdeo.com/2008/09/19/simulating-the-raid-failure/)，但是对于HDFS这种不开启RAID的文件系统可能就必须用[SCSI fault injection test tool](http://sourceforge.net/projects/scsifaultinjtst/)或者[SystemTap](https://sourceware.org/systemtap/)这类工具了。也有一下小型开源项目如[fsdisk](http://www.thirdmartini.com/index.php/Linux_Disk_Failure_Simulation_Driver)提供了简便的接口去注入错误，另一种简单的方法是通过命令dd if=/dev/zero of=/dev/sdb/sdb1 bs=1024 count=102400去破坏分区的信息，破坏前备份一下然后通过dd即可回去，唯一的缺点是恢复后需要重新mount才能接受正常的读写请求。实际上Linux已经为开发者提供了很全面的错误注入框架和[使用手册](http://lxr.free-electrons.com/source/Documentation/fault-injection/fault-injection.txt)，我们参考这篇[文章](http://blog.wpkg.org/2007/11/08/using-fault-injection/)也可以对我们的文件系统进行错误注入。

### DiskFull
> 磁盘满表明没有可用空间了，最直接而且最真实的方法是创建大文件占满磁盘，我们可以使用命令dd if=/dev/zero of=/$path/tst.img bs=1M count=20K来创建超大文件把磁盘占满，恢复也很简单，只要把指定目录的这个文件删除就可以了。当然这样我们需要知道生成文件所用的时间，才能观察被测程序再磁盘满的情况下的表现。通过[创建大量小文件](http://www.zhukun.net/archives/5816)可以使iNode节点耗尽，导致无法创建新文件，也可以达到磁盘资源不足的故障。

### DiskSlow
> 要模拟磁盘访问速度慢，目前我们考虑使用[fio](https://www.linux.com/learn/tutorials/442451-inspecting-disk-io-performance-with-fio/)这个压测工具，通过对磁盘进行大量的访问，必然导致其他进程的磁盘访问速率下降，kill掉这个进程相当将磁盘恢复为正常状态，当然这种方式很难控制磁盘速率减慢的程度。

### NetworkBandWidthLimit
> 模拟服务器网络带宽限制最好的工具是tc（traffic control），而且是由Linux内核提供的，在服务器中输入命令tc qdisc add dev eth0 root tbf rate 5800kbit latency 50ms burst 1540即可限制带宽为5800kbit，如果需要恢复则只需执行命令tc qdisc del dev eth0 root tbf rate 5800kbit latency 50ms burst 1540。这样我们在本地或者远程都可以控制测试服务器的带宽，进程观察被测程序在带宽受限时的表现。

### NetworkDelay
> 模拟网络延迟和下面的网络故障都是通过tc来实现的，我们通过tc qdisc add dev eth0 root netem delay 300ms就可以对所有请求都增加300毫秒的延时，然后通过tc qdisc del dev eth0 root netem delay 300ms即可恢复过来，这里一篇[文章](http://blog.sina.com.cn/s/blog_71ad0d3f0100y54f.html)介绍了简单的用法，更详细的介绍可以参考[这里](http://www.linuxfoundation.org/collaborate/workgroups/networking/netem)。注意设置网络延迟后包括ssh操作都会感觉到明显的延迟，在测试时必须保证我们能够远程恢复过来。

### NetworkPackageCorrupt
> 要模拟包损坏，我们看到一些[开源项目](https://github.com/Netflix/SimianArmy/blob/master/src/main/resources/scripts/networkcorruption.sh)也是以这种形式来注入错误的，通过tc qdisc add dev eth0 root netem corrupt 5%破坏并利用tc qdisc del dev eth0 root netem corrupt 5%来恢复。

### NetworkPackageLost
> 模拟丢包命令sudo tc qdisc add dev eth0 root netem loss 5%可设置服务器5%的丢包率，执行sudo tc qdisc del dev eth0 root netem loss 5%恢复。设置网络丢包的命令一旦执行后，所有请求都有可能丢失，包括我们发出的恢复命令，所以在模拟这种故障的时候我们的恢复命令需要多次重试以保证服务器真的恢复过来了。

### NetworkUnavailable
> 如果希望网络不可用，我们可以参考[这里](https://github.com/Netflix/SimianArmy/blob/master/src/main/resources/scripts/nullroute.sh)使route都不可用的，这样我们要恢复就很困难了。所以我们期望的网络不可用应该是针对特定进程或者端口的不可用，于是可以考虑使用iptable这个Linux防火墙，iptables -A OUTPUT -p tcp --dport 3306 -j DROP这个命令就是屏蔽3306端口的所有请求，对于监听这个端口的服务相当于不可用了，而通过iptables -D OUTPUT -p tcp --dport 3306 -j DROP即可恢复。iptable的用法可参考这篇[文章](http://terminalinflection.com/using-iptables-to-simulate-service-interruptions/)，而详细的原理与配置可参考这个[文档](http://www.ibm.com/developerworks/cn/linux/network/s-netip/)。

