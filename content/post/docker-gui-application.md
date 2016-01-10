+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "docker gui application"

+++



## Docker与GUI应用

[Docker](https://github.com/docker/docker)是开源的容器技术，容器是比虚拟机更轻量的虚拟化技术，优势是隔离软件的运行环境并且最小化其额外的开销。隔离运行环境的好处之一就是可以轻易创建干净的开发环境，而在我第一次Docker分享中，大家最关心的问题就是“Docker可以运行GUI应用吗”。

Docker作为虚拟化技术，并没有改变进程的运行方式和图像显示协议，因此Docker是可以运行GUI应用的。就像在裸机中要运行图形界面，我们有必要了解下Linux的[X Window协议](http://zh.wikipedia.org/wiki/X_Window%E7%B3%BB%E7%B5%B1%E7%9A%84%E5%8D%94%E8%AD%B0%E5%92%8C%E6%9E%B6%E6%A7%8B)。在Linux中，一个GUI应用的显示都经过X Window这个C/S模型，简单概括就是X Server在后台运行，接受X Client的请求，并将显示的结果通过特定安全的协议返回。

运行Docker GUI应用的原理与之类似，下面将一步步带领大家创建基于Docker的图形化程序。

## Dockerized OpenOffice

![](/images/openoffice_and_docker.png)

[Dockerized-openoffice](https://github.com/tobegit3hub/dockerized-openoffice)就是运行在容器内的GUI应用，执行命令`docker run -d -p 6080:6080 tobegit3hub/dockerized-openoffice`然后在浏览器打开<http://127.0.0.1:6080/vnc.html>就可以看到图形界面的OpenOffice应用。

其实现玄机就在[Dockerfile](https://github.com/tobegit3hub/dockerized-openoffice/blob/master/Dockerfile)中，代码中有安装`apt-get install -y lxde x11vnc xvfb`这一步，就是安装我们前面提到的X Server，这样通过特定的VNC客户端就可以访问这个GUI应用了。这里我们选择[noVNC](https://github.com/kanaka/noVNC)客户端来连接我们的Dockerized应用，导入noVNC源码，启动服务器，打开6080端口，这样我们`docker run`以后就可以通过浏览器来访问GUI应用了。

实际上这里我们把整个Linux桌面管理器都装了，因此运行Firefox等一切应用都是可能的。

## 参考链接

* <https://github.com/fcwu/docker-ubuntu-vnc-desktop>

使用VNC和noVNC搭建Ubuntu环境的实例，无论是源码还是使用的技术都值得参考。

* <http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/>

在Docker运行NetBeans等开发环境，虽然使用价值不大但Docker就真的做到了。

* <http://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container>

运行Firefox而不需要安装Firefox，整个Dockerfile也相当简单。

* <https://blog.docker.com/2013/07/docker-desktop-your-desktop-over-ssh-running-inside-of-a-docker-container/>

Docker官方文档介绍通过SSH运行桌面系统，使用的是Xpra。