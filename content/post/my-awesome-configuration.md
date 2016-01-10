+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "my awesome configuration"

+++



<pre>
–auto run app
awful.util.spawn_with_shell(“ibus-daemon –xim”)
awful.util.spawn_with_shell(“nm-applet”)
awful.util.spawn_with_shell(“gnome-power-manager”)
</pre>

已经不需要了，通过脚本可以更灵活地启动~