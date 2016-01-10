+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "implement your wordpress theme zh"

+++



## 简介

[WordPress](https://wordpress.org/)是一个PHP实现的CMS内容管理系统，大家都很喜欢用它来搭建个人博客，因为它安装简单，功能强大，而且可拓展性非常好。你可以使用别人制作的各种免费付费主题，当然也可以自己实现，从Html、Css到JavaScript完全个人定制，而且系统已经实现了数据库操作和后台功能，通过API调用很容易就能实现各种高级功能。

[GoddnessTheme](https://github.com/tobegit3hub/GoddessTheme)是我自己实现的WordPress主题，代码非常简单，只是通过Bootstrap来美化样式。通过这个项目可以知道实现一个主题所需要的全部要素，模仿里面API的使用，你也可以定制一个符合自己要求，有特色功能的个性化网站。演示页面在[这里](http://www.chendihao.cn/)。

## 实现步骤
1. 按照WordPress[官方文档](http://codex.wordpress.org/Theme_Development)创建必须的index.php、single.php等文件。
2. 使用WordPress提供的API获取Post等内容，嵌入到你的PHP代码中。
3. 搭建PHP、MySQL开发环境（Windows可选择Wamp程序）进行调试。
4. 可添加[Bootstrap](http://getbootstrap.com/)快速美化你的样式，加入相应的class和用于排版的div。
5. 最后要截图保存为screenshot.png，然后打包你的主题上传到服务器上。

## 源码分析

### index.php

<https://github.com/tobegit3hub/GoddessTheme/blob/master/GoddessTheme/index.php>

这是显示博客列表的主页面，所以直接调用have_posts()和the_post()循环遍历Post内容，然后一般都把the_title()、the_time()和the_content()提取出来，使用Bootstrap的好处就是你连样式的Css都可以懒得写了，这里也没有太多复杂的逻辑判断。后面就是引入header、sidebar、footer和使用一个插件来分页。

### header.php

<https://github.com/tobegit3hub/GoddessTheme/blob/master/GoddessTheme/header.php>

这是Bootstrap标准的菜单栏，而且是响应式布局，通过wp_list_pages()从系统中所有的页面信息，这样只要在系统后台添加页面也能马上展示到菜单栏上。同时这里使用了自己的搜索框，要实现搜索功能，就参考原来的标签的属性，添加`name="s"`后就将这个后台功能加到你的控件上了。

### footer.php

<https://github.com/tobegit3hub/GoddessTheme/blob/master/GoddessTheme/footer.php>

这里列举了一些用到的工具，还有执行一条SQL语句，获得网站最近的更新时间。

### sidebar.php

<https://github.com/tobegit3hub/GoddessTheme/blob/master/GoddessTheme/sidebar.php>

几个经典的函数拿到分类、archive、最近的Post和最多的Comment。

### page.php

<https://github.com/tobegit3hub/GoddessTheme/blob/master/GoddessTheme/page.php>

跟主页是类似的，不过这里只需要显示一个Post的内容。

### functions.php

<https://github.com/tobegit3hub/GoddessTheme/blob/master/GoddessTheme/functions.php>

最后的这个函数是Bootstrap用与响应时布局的，当菜单栏太多项时自动缩回。
