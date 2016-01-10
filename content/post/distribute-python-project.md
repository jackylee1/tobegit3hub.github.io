+++
date = "2014-11-10T08:35:32+08:00"
draft = true
title = "distribute python project"

+++



## 简介

根据DRY（Don't Repeat Yourself）原则，我们都会把通用的代码封转成Package发布，让其他人更容易复用。这是一个通用的原则，所以每种编程语言都有各自的Package Manager来管理依赖和发布项目，Maven之于Java，Npm之于JavaScript，Phar之于PHP，Bower之于Web，Gem之于Ruby，而Python的主流是Pip。

使用Pip的好处有很多，首先是依赖的管理，任何人都可以通过统一的`pip install`安装封装过的类库，告别源码依赖。在<https://pypi.python.org/pypi>可以查找所有可重用的Package，而且根据Python原生的setuptools很容易分发自己的Python项目。

## PyPI

Pip成为事实标准后，PyPI（Python Package Index）成了默认的公开仓库。任何人都可以把自己的项目发布到那里，流程也很简单，在<https://pypi.python.org/pypi>注册个账号，然后registry你的应用信息，最后上传代码。没有人审核吗？确实没人审核，估计只要名字不重就可以了，注册时要勾一个协议说是只发布与Python相关的东西。

应用一旦上传，任何人都可以`pip install`安装，对公开的项目很方便，但私有项目呢？这就跟Maven是一样的，大家都可以访问公有仓库，如果只想部分人共享只能自己搭私有Index。有个项目Pypicloud可以做这个，不过Python搭私有仓库的比Java少很多，估计和Python圈子比较开放有关。

## Setup.py

打包Python项目很简单，写一个名为setup.py的文件即可，我以FDS Python SDK为例介绍一下。Setup.py符合Python语法，只要填上项目的基本信息和依赖信息即可。

```
import os
import sys

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup

setup(
    name='galaxy-fds-sdk',
    version='1.0.0',
    author='haxiaolin',
    author_email='haxiaolin@xiaomi.com',
    include_package_data=True,
    install_requires = ['requests>=1.4.3'],
    #url='https://github.com/',                                                                                                                                                                                     
    license='Apache License',
    packages=['fds', 'fds.auth', 'fds.auth.signature', 'fds.model'],
    description='Galaxy FDS SDK',
    long_description=open('README.md').read(),                                                       )
```

比较重要的是name，这里是“galaxy-fds-sdk”，以后别人就这样用了`pip install galaxy-fds-sdk`。很重要的还有install_requires，表示依赖的项目，其他人安装这个Package时应该会先去检查所依赖的其他包。最重要的是packages这项，表示了你要发布哪些module，Python中只要有\__init__.py的文件夹就认为是一个module，这里必须把你想让别人用的代码全部列出来。其他的author、licnese和long_description这些只是影响在PyPI官网看到的Package介绍信息。

写好setup.py可以本地测试一下，最简单就是`python setup.py install`直接安装在本地，然后开个终端检查能否import这些模块。

补充一点，我们可以看看[requests](https://github.com/kennethreitz/requests)这个项目的代码，它的setup.py写了`packages = [requests']`，确实引入了项目根目录requests文件夹中的内容，但它是如何让别人直接调用`requests.get()`的呢？如果不特殊处理，按照Python的语法正常应该这样调用`requests.api.get()`。原理就在它requests模块下的\__init__.py写了`from .api import request, get, head, post, patch, put, delete, options`，这样就可以直接调用import的所有方法了。

## 发布

写好了setup.py，要把自己的项目发布到仓库让别人用就很简单了。

1. 在<https://pypi.python.org/pypi>注册一个账号。
2. 本地执行`python setup.py register`，这时需要填用户名和密码。
3. 本地执行`python setup.py sdist upload`即可。

我写了个最简单的[hello_pip](https://github.com/tobegit3hub/hello_pip)项目，可以了解发布到Pip仓库最简单的配置和代码。

## 总结

如果是对外公开的Python项目，发布到PyPI应该是最基本的要求，Github上的开源项目一般都有这样两个Badge。用户可以根据需要选择不同的版本，而不是`python setup.py install`安装最新版或者直接拉源码`checkout branch`来用。

[![PyPi version](https://pypip.in/v/hello_pip/badge.png)](https://pypi.python.org/pypi/hello_pip) [![PyPi downloads](https://pypip.in/d/hello_pip/badge.png)](https://pypi.python.org/pypi/hello_pip)

使用setup.py是很简单的，建议所有Python项目都用，即使是小脚本也可以省去源码依赖的各种问题。