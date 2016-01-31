+++
date = "2015-12-08T09:32:46+08:00"
draft = true
title = "OpenStack项目运行单元测试"

+++

## 单元测试介绍

单元测试（Unit test）是对代码的细粒度测试，一般每写一个函数都需要写对应的测试用例。运行单元测试不应该依赖外部环境，如果依赖其他程序，可以通过mock来模拟环境。

Python项目使用标准的单元测试库来写测试用例，并可以通过业界标准工具tox来运行，部分OpenStack项目还提供了run_tests.sh脚本来简化运行。

## 准备环境

安装Python，通过apt-get install python-dev

安装pip，通过apt-get install python-pip

安装virtualenv，通过pip install virtualenv

安装tox，通过pip install tox

安装postgres，通过apt-get install libpq-dev

安装xml和xslt库，通过apt-get install libxml2-dev libxslt1-dev

安装ffi库，通过apt-get install libffi-dev

## 使用run_tests.sh

以manila项目为例：

```
git clonehttps://github.com/openstack/manila.git

cd manila/

./run_tests.sh
```

## 使用tox

```
tox -epy27 --
```

## 使用testr

```
testr run
```

## 检查UT覆盖率

```
./run_tests.sh --coverage
```

运行UT加上参数，可以生成显示覆盖率的HTML文件，直接用浏览器打开就可以了，google-chrome covhtml/index.html。

## Troubleshoot

报错from oslo.config import cfg，ImportError: No module named config
因为项目依赖的oslo的版本和requirements.txt的版本不对，一般是使用了太新的oslo库，需要限制其最高版本。

```
oslo.config>=1.6.0,<=1.7.0
```