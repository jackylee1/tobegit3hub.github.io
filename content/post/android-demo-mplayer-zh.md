+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "android demo mplayer zh"

+++



## 简介

如果你正在学习Android应用开发，这里有一个入门级的应用程序[mpleyer](https://github.com/tobegit3hub/mplayer)，你可以了解到一个Android项目开发的基本要点和步骤。

## 分析

Android项目有一定的目录规范，必须写AndroidManifest.xml，这些都可以通过国内外的资料来学习。我们来讲解一个比较通用的需求，首先是客户端程序展示一个页面供用户输出，用户点击后可以向服务器发出请求并显示响应的结果。[MplayerController](https://github.com/tobegit3hub/mplayer/tree/master/MplayerController)就是这样一个简单的客户端，通过阅读源代码你可以知道它的实现细节，这里也会讲一下开发的步骤。

## 实现

### MainActiviy.java

<https://github.com/tobegit3hub/mplayer/blob/master/MplayerController/src/cn/chendihao/mplayercontroller/MainActivity.java>

每个Android应用都需要至少一个Activity，而这个应用也只有这个，并且已经在AndroidManifest.xml中注册。这里代码指定使用activity_main.xml描述的布局，还处理了比较典型的响应菜单按钮和返回按钮，并且也涉及到一些Java Socket编程的知识。

### activity_main.xml

<https://github.com/tobegit3hub/mplayer/blob/master/MplayerController/res/layout/activity_main.xml>

这个MainActivity的布局也很简单，基本是自描述的，有一个用户输入的EditText和发送命令的ImageButton。

### main.xml

<https://github.com/tobegit3hub/mplayer/blob/master/MplayerController/res/menu/main.xml>

当然这个项目也实现的菜单的相应代码，而菜单的配置最好也独立成自描述的XML文件，可以看出这里的三个菜单选项和对应的id，回顾MainActivity.java的代码如何来调用这些Menu。
