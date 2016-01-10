+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "build go project for all platforms"

+++



使用Go可以编译各平台的二进制文件，下载对应的文件就可以直接运行了。更好的是可以在一个平台交叉编译所有平台的二进制文件，我以[runscripts](https://github.com/runscripts/runscripts)为例介绍完整的用法。

首先，默认安装的Go是不支持交叉编译的（只安装本地需要的包），要支持交叉编译可以到/usr/local/go/src/目录执行`sudo CGO_ENABLED=0 GOOS=linux GOARCH=amd64 ./make.bash`。由于我不是源码安装的，所以找不到这个目录，于是在Mac上使用Homebrew重新安装Go，命令是`brew install --cross-compile-all go`。

然后，我们到$GOPATH/src/github.com/runscripts/runscripts目录执行`go build`，这样会生成本平台的runscripts二进制文件。

如果想编译64位Linux的应用呢，只需要执行`CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build`即可。其中GOOS还可以选darwin、freebsd、windows等，GOARCH还可以选386和arm等。更多编译命令可以参考[构建run](https://github.com/runscripts/runscripts/tree/master/build)。

所有支持编译的平台如下:

* darwin/386
* darwin/amd64
* linux/386
* linux/amd64
* linux/arm
* freebsd/386
* freebsd/amd64
* openbsd/386
* openbsd/amd64
* windows/386
* windows/amd64
* freebsd/arm
* netbsd/386
* netbsd/amd64
* netbsd/arm
* plan9/386


总结，Go是个好东西，代码写通用一些争取支持Windows。

