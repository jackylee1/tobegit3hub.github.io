+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "awesome adjust volumn"

+++



## 最终解决办法

`gnome-sound-applet &`

## 失败尝试

* [Awesome调节音量不再依赖GNOME](http://lilydjwg.is-programmer.com/2011/12/5/awesome-volumn-widget.31160.html)
* 配置文件应该是新建~/.config/awesome/rc.lua，而且在/etc/xdg/awesome/rc.lua
* amixer -q sset Master 10%+ unmute 有时对耳机有效，差点搞坏了
* rc.lua多加了会导致崩溃幸好.bak，可见的调节按钮要加到wibox中
