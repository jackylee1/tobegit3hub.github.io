+++
date = "2016-01-24T10:37:59+08:00"
draft = true
title = "use saws for aws services"

+++

## 介绍

AWS是Amazon推出的业界领先的云服务，提供了权限管理、虚拟机、数据库等诸多服务。

如果对IAM服务感兴趣可以参考 <http://www.infoq.com/cn/articles/aws-iam-dive-in> 。

由于AWS服务非常多，开发者使用并不方便，因此一般会使用命令行工具aws和命令行增强工具saws。

## Saws

[Saws](https://github.com/donnemartin/saws)是比aws官方命令行更好用的开源工具，可以直接通过pip安装。

```
pip install saws
```

使用前需要填写AWS的AKSK信息，详情可参考 https://github.com/aws/aws-cli#getting-started

```
aws configure
```

然后就可以直接登录使用了。

```
saws

saws> aws iam list-users
```

