+++
date = "2013-02-12T08:35:28+08:00"
draft = true
title = "wordpress change to chinese"

+++



在主机wordpress根目录下的/wp-content目录中创建名为languages的目录。

把解压得到的zh_CN.mo文件上传到languages目录中。

修改wordpress根目录中的wp-config.php文件，把第15行的

> define (’WPLANG’, ”)

修改为：

> define (’WPLANG’, ‘zh_CN’)