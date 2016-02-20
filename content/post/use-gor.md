+++
date = "2016-02-15T12:27:34+08:00"
draft = true
title = "use gor"

+++

## 介绍

gor是目前常用的流量复制工具，可以在将生产环境的流量无缝拷贝的staging环境进行开发和测试，项目开源地址 https://github.com/buger/gor.git

## 安装gor

安装golang，配置GOPATH

``` 
mkdir $GOPATH/buger
git clone https://github.com/buger/gor.git
go get
go build
```

## 使用gor

如果是本地测试，可以直接执行。

```
sudo ./gor --input-http :28019 --output-http "http://staging.com"
```

如果生产环境多台服务器，可以执行。

```
sudo gor --input-raw :80 --output-tcp replay.local:28020
 
sudo gor --input-tcp replay.local:28020 --output-http http://staging.com
```