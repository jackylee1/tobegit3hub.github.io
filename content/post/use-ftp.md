+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "use ftp"

+++



## 背景

除了Windows，Linux和Mac对Android手机平板的支持都不好，拷贝文件都相当麻烦。以前是`adb`来搞的，现在不折腾了，发现MIUI文件管理可以开启FTP，而Linux和Mac原本就安装了`ftp`命令，相当于什么都不用配置了。

## 基础

FTP基本命令只有几个，完全符合Linux语法，下面演示常用的。

```
ftp 127.0.0.1 10080
ftp> cd /sdcard/Download/
ftp> put /home/tobe/mountmentvalley.apk
ftp> lcd /home/tobe/temp/
ftp> get /sdcard/Download/mountmentvalley.apk
ftp> mget /scard/Download/*.apk
```

## 参考

* <http://tecadmin.net/download-upload-files-using-ftp-command-line/>