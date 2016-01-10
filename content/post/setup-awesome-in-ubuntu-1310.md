+++
date = "2013-12-05T08:35:30+08:00"
draft = true
title = "setup awesome in ubuntu 1310"

+++



## Configuration 

* add /usr/share/gnome-session/sessions/awesome.session

<pre>
[GNOME Session]
Name=Awesome session
RequiredComponents=awesome;gnome-settings-daemon;
DesktopName=Awesome
</pre>

* add /usr/share/applications/awesome.desktop

<pre>
[Desktop Entry]
Version=1.0
Type=Application
Name=Awesome
Comment=The awesome launcher!
TryExec=awesome
Exec=awesome
</pre>

* add /usr/share/xsessions/awesome-gnome.desktop

<pre>
[Desktop Entry]
Name=Awesome GNOME
Comment=Dynamic window manager
Exec=gnome-session --session=awesome
TryExec=awesome
Type=Application
X-LightDM-DesktopName=Awesome GNOME
X-Ubuntu-Gettext-Domain=gnome-session-3.0
</pre>

* edit /etc/xdg/autostart/gnome-settings-daemon.desktop

<pre>
[Desktop Entry]
Type=Application
Name=GNOME Settings Daemon
Exec=/usr/lib/gnome-settings-daemon/gnome-settings-daemon-localeexec
OnlyShowIn=GNOME;Unity;Awesome;
NoDisplay=true
X-GNOME-Autostart-Phase=Initialization
X-GNOME-Autostart-Notify=true
X-GNOME-AutoRestart=true
X-Ubuntu-Gettext-Domain=gnome-settings-daemon
</pre>

## Usage

* choose Awesome in gdm

## Reference

* <http://awesome.naquadah.org/wiki/Quickly_Setting_up_Awesome_with_Gnome>