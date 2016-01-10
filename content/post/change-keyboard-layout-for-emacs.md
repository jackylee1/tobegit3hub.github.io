+++
date = "2013-05-14T08:35:29+08:00"
draft = true
title = "change keyboard layout for emacs"

+++



* xev to check the keyboard layout

<pre>
Caps 66 Caps_Lock
LControl 37 Control_L
Windows 134 Super_R
Menu 135 Menu
RControl 105 Control_R
Esc 9 Escape
</pre>

* xmodmap to change 

<pre><code>
# exchange Caps and LControl                                                                                                 
xmodmap -e "remove Lock = Caps_Lock"
xmodmap -e "remove Control = Control_L"
xmodmap -e "keycode 66 = Control_L"
xmodmap -e "keycode 37 = Caps_Lock"
xmodmap -e "add Lock = Caps_Lock"
xmodmap -e "add Control = Control_L"

# change RWin as Control                                                                                                     
xmodmap -e "clear mod4"
xmodmap -e "keycode 134 = Control_R"
xmodmap -e "add Control = Control_R"

# change Menu as RSuper                                                                                             
# xmodmap -e "keycode 135 = Escape"                                                                                 
xmodmap -e "keycode 135 = Super_R"
</code></pre>