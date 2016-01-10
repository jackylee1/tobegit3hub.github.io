+++
date = "2016-01-10T08:35:29+08:00"
draft = true
title = "use multi screen in ubuntu"

+++



If you have two monitors, just configure and use them. In Ubuntu, you can search “display setting”, however, it occurs some unknown errors. Just use `xrandr`, the original commandline tool to setup your devices. Ordinarily, you may rotate your monitor and expend to another one.

Here is my .MultiScreen.sh:

<pre>
xrandr -o left
xrandr –output HDMI2 –left-of VGA1 –auto
</pre>