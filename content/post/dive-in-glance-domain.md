+++
date = "2016-01-22T16:54:25+08:00"
draft = true
title = "深入理解Glance domain实现机制"

+++

## 介绍

Glance的实现核心是Domain model，也就是一个请求过来会通过一些列domain，类似Python的decorator和Paste的pipeline，依此解耦地实现认证、配额、持久化等功能。

## Domain概念

实现Domain model项目提出了多个概念，第一个Proxy，我们定义了基类所包含的函数，实现这些函数的子类就是Proxy。

其次是Gateway，就是显式调用和组合Proxy的类。例如我们定义了LoggerProxy和ValidatorProxy，我们可以写个Gateway根据用户给定的参数返回不同的Proxy。

然后是Helper，这可以是普通工具类也可以对Proxy的封装，在Factory中会用到。例如我们封装一个Proxy对象，实现两个函数，一个返回Proxy，一个返回Proxy的父类。

最后是Factory，就是一个工厂类，提供一个get()函数，通过函数指定调用哪些Proxy。例如我们创建LoggerFactory和ValidatorFactory，他们都实现了generate()函数，函数里用Helper工具类，然后一层一层调用下去。