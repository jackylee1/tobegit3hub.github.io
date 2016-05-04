+++
date = "2016-05-04T10:25:42+08:00"
draft = true
title = "Basic RPM Commands"

+++

## RPM Commands

查看包的版本。

```
rpm -q openstack-nova-api
```

查看所有安装的包。

```
rpm -qa | grep "nova"
```

查看一个文件属于哪个包。

```
rpm -qf /etc/nova/nova.conf
```

查看一个包有哪些文件。

```
rpm -ql openstack-nova-api
```

查看一个包依赖哪些包。

```
rpm -q --requires openstack-nova-api
```

查看一个包的详情。

```
rpm -qi openstack-nova-api
```

## YUM Commands


安装。
```
yum install
```

卸载。

```
yum remove
```

升版本。
```
yum update
```

降版本。

```
yum downgrade
```

搜索。

```
yum search
```

查看所有版本的包。

```
yum info --showdeplicates
```

## Reference

* fedora 提供的⽂档，⾮常全⾯ <https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/index.html>
* ⽐较简短的⽂档，关于如何buildrpm包 <https://fedoraproject.org/wiki/How_to_create_an_RPM_package>
* 很多⼩技巧 <https://wiki.centos.org/zh/TipsAndTricks/YumAndRPM>
* ⽂档⽐较⽼，但是仍然可⽤ <https://www.ibm.com/developerworks/cn/linux/l-lpic1-v3-102-5/>