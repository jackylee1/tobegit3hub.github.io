+++
date = "2016-01-10T08:35:31+08:00"
draft = true
title = "install tsocks in mac"

+++



Sometimes `brew install tsocks` fails, and you should add a newer brew formula for tsocks.

Tsocks is really useful to connect with proxy in ternimal, and it's easy to configurated.

## Process

* Add /usr/local/Library/Formula/tsocks.rb
* `brew install –HEAD tsocks`

## Reference

* <http://www.blogjava.net/sean/archive/2014/05/11/413382.html>