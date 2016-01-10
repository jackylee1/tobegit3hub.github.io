+++
date = "2013-01-28T08:35:28+08:00"
draft = true
title = "bug from miui v4"

+++



The log from MIUI:

<pre>
D/scan (11937): SCREEN OFF

I/CpuGovernorService( 312): intent action: android.intent.action.SCREEN_ON

I/ResourceManager( 312): load image unlock_top_p.png

V/AudioHardwareMSM8660( 136): setParameters() screen_state=on

D/scan (11937): SCREEN ON

I/ResourceManager( 312): load image music_pre_n.png

onNotify: miui.app.screenelement.NotifierManager$BatteryNotifier@430842f0

I/ResourceManager( 312): load image music_pre_n.png

I/WindowManager( 312): Lock screen displayed!

D/FramerateTokenList( 312): requestFramerate: 0.0 by:miui.app.screenelement.elements.FramerateController@431eb998

There are certain events that Android does not want to start up new processes for, so the device does not get too slow from all sorts of stuff all having to run at once. ACTION_SCREEN_ON is one of those. See this previous question for light blue advice on that topic.

java.lang.SecurityException: Permission Denial: not allowed to send broadcast android.intent.action.SCREEN_OFF from pid=3244, uid=10046
</pre>