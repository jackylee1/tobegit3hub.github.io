+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "implement of tpp zh"

+++



### 0. 项目简介
[Tpp](http://www.ngolde.de/tpp.html)全称Text Presentation Program，是一个Ruby实现的纯文本展示程序，它使用ncurses库可以在Linux平台上实现动画、颜色的显示和响应键盘的输入。一个最基本的example.tpp文件如下，执行`tpp example.tpp`即可在终端显示两页slide，<kbd>Space</kbd>显示下一页，<kbd>b</kbd>前一页，<kbd>q</kbd>退出。

    # sample.tpp
    --title Text Power Point
    --date today

    --newpage
    --heading Funny topic

在Github的[这个项目](https://github.com/cbbrowne/tpp)可以查看tpp的源代码，发现这个程序仅仅是一个1767行的Ruby脚本，虽然源码只有一个文件，但这个项目居然把Makefile、man page、vim插件和emacs插件都做了，这个小项目基本囊括了大型Linux项目所需要的一切，还是很值得我们去研究的。

### 1. Tpp脚本
首先我们可以看一下[tpp.rb](https://github.com/cbbrowne/tpp/blob/master/tpp.rb)这个最重要的文件，它的功能就是读取一个.tpp文件的内容，然后使用ncurses显示出来并响应用户的操作。运行程序前必须安装Ruby和ncurses-ruby这个gem，否则程序就会推出。虽然项目没有按文件划分模块，不过内部还是分成逻辑比较清晰的几个部件，包括分析.tpp文件的FileParser，用于显示页面的TppVisualizer和处理用户交互的TppController。理解各个组建后看源代码就很简单了，唯一需要注意的是ncurses这个库的使用，下面就是程序主逻辑用于绘图的部分代码。

    loop do
      wait = false
      @vis.draw_slidenum(@cur_page + 1, @pages.size, false)
      # read and visualize lines until the visualizer says "stop" or we reached end
      begin
        line = @pages[@cur_page].next_line
        eop = @pages[@cur_page].eop?
        wait = @vis.visualize(line,eop)
      end while not wait and not eop
      # draw slide number on the bottom left and redraw:
      @vis.draw_slidenum(@cur_page + 1, @pages.size, eop)
      @vis.do_refresh
    end

### 2. Makefile
接下来可以看一下小型项目的Makefile可以怎么写，Makefile用于安装和卸载一个程序，对于一个脚本来说就太简单了，尤其是它没有任何依赖的时候，我们可以看看tpp的[Makefile](https://github.com/cbbrowne/tpp/blob/master/Makefile)是怎么写的。

    BIN = tpp  
    prefix=/usr/local
    INSPATH= $(prefix)/bin/
    DOCPATH = $(prefix)/share/doc/tpp
    MANPATH = $(prefix)/share/man/man1

    all:
    	@echo "TPP doesn't need to be built. Run \`make install' in order to install it."

    install :
    	mkdir -p $(DOCPATH)
    	install -m644 DESIGN CHANGES COPYING README THANKS $(DOCPATH)
    	install -m644 doc/tpp.1 $(MANPATH)
    	install tpp.rb $(INSPATH)$(BIN)
    	mkdir -p $(DOCPATH)/contrib
    	mkdir -p $(DOCPATH)/examples
    	install -m644 examples/* $(DOCPATH)/examples/
    	install -m644 contrib/* $(DOCPATH)/contrib/

    uninstall :
    	rm -f $(INSPATH)$(BIN)
    	rm -rf $(DOCPATH)
    	rm -f $(MANPATH)/tpp.1*

### 3. Man page
然后我们还可以看一下怎么写一个man page，对于任何Linux命令来说，man page实在太重要了，因为里面包含了这个命令的所有参数和用法，像Dropbox虽然为用户提供了命令行脚本，但是我在使用的时候还是更愿意通过man来查用法而不是上它的官网看文档。看过tpp的[tpp.1](https://github.com/cbbrowne/tpp/blob/master/doc/tpp.1)，马上消除了我对写man page的恐惧，因为实在是太简单了，可以截取其中一段。


    .TH  TPP "1" "April 2007" "tpp 1.3.1" "User Commands"
    .SH NAME
    TPP - Text Presentation Programenter preformatted text here
    .SH SYNOPSIS
    .B tpp  
    <\fIOPTIONS\fR> <\fIFILE\fR>
    .SH DESCRIPTION
    .PP
    Tpp stands for text presentation program and is an ncurses-based
    presentation tool. The presentation can be written with your favorite
    editor in a simple description format and then shown on any text
    terminal that is supported by ncurses - ranging from an old VT100 to the
    Linux framebuffer to an xterm.

### 4. Vim插件与Emacs插件
感兴趣还可以看一下它的vim插件[tpp.vim](https://github.com/cbbrowne/tpp/blob/master/contrib/tpp.vim)和emacs插件[tpp-mode.el](https://github.com/cbbrowne/tpp/blob/master/contrib/tpp-mode.el)是如何实现的。由于tpp功能单一，它的插件逻辑也很简单，甚至还可以以此作为例子学习编辑器的插件开发呢。

