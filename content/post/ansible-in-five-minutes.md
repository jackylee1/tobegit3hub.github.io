+++
date = "2016-03-29T22:55:21+08:00"
draft = true
title = "ansible in five minutes"

+++

## 什么是Ansible

Ansible是自动化运维工具，可以批量管理服务器并执行配置管理等相关操作，功能强大并且简单易用。

## 安装Ansible

```
pip install ansible
```

## 通过Ansible执行命令

使用Ansible可以在任意服务器批量执行任意命令，例如最简单的ping。

```
ansible 127.0.0.1 -m ping
```

或者是执行任意的Shell命令，都非常简单。

```
ansible 127.0.0.1 -m command -a 'echo "hello"'
```

## 编写inventory文件

Ansible对主机组进行划分，然后卸载inventory文件中，最简单的inventory应该是这样的hosts文件。

```
[local]
127.0.0.1
```

然后可以直接执行命令。

```
ansible -i ./hosts local  -m command -a 'echo "hello"'
```




