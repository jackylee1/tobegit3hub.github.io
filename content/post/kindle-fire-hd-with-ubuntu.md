+++
date = "2013-05-21T08:35:29+08:00"
draft = true
title = "kindle fire hd with ubuntu"

+++



If you are a programmer using Linux, you could find that the driver of Kindle Fire HD doesn’t work perfectly. You’re unable to access its storage. That means you could not push file or setup application for your tablet through your computer. One solution is to use Microsoft Windows, but the better choise is playing with adb.

1. You should setup the adb environment.
2. `adb device` to dectect the device.
3. `adb install foo.apk` to install any application you want.
4. `adb push localFile kindlePath` to push documents such as `/sdcard/Documents/.
5. If you don’t know the path, use `adb shell`.
