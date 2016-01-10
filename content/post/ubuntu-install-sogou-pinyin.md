+++
date = "2013-12-07T08:35:30+08:00"
draft = true
title = "ubuntu install sogou pinyin"

+++



## Method

* sudo apt-get remove ibus
* sudo apt-get remove fcitx*
* sudo add-apt-repository ppa:fcitx-team/nightly
* sudo apt-get update
* sudo apt-get install fcitx-sogoupinyin
* sudo apt-get install im-switch
* im-switch -s fcitx -z default
* restart the host
* add Sogou Pinyin in fcitx

## Reference

* <http://blog.sciencenet.cn/blog-1148100-741831.html>