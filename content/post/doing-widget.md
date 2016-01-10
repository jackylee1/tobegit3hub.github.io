+++
date = "2012-12-30T08:35:27+08:00"
draft = true
title = "doing widget"

+++



## 简介

DoingWidget是一个只有单行文本输入框的Android Widget，用户通过输入当前的任务，让自己更清楚知道现在开机是为了干什么。因为很简单，所以可以作为例子来熟悉Android平台下的<strong>Widget</strong>是怎样编码实现的，程序主要是根据《疯狂Android讲义》里面的DesktopApp实例。

## 步骤

1.1.开发一个继承<strong>AppWidgetProvider</strong>的子类，实际上是一个BroadcastReceiver。

1.2.重写<strong>onUpdate</strong>等成员函数，用于更新桌面控件。

1.3.创建<strong>RemoteViews</strong>对象，用于指定界面布局文件。

1.4.创建<strong>ComponentName</strong>对象，在update时要用到。

1.5.调用<strong>AppWidgetManger</strong>更新桌面控件。

1.6.在<strong>AndroidManifes</strong>t中注册。

(1.7.新建xml文件来<strong>描述</strong>Widget的基本信息。)

## 源代码

### DoingWidget.java

<pre>
package com.tobe;

import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.ComponentName;
import android.content.Context;
import android.widget.RemoteViews;

public class DoingWidget extends AppWidgetProvider {
	@Override
	public void onUpdate(Context context, AppWidgetManager appWidgetManager, int[] appWidgetIds) {

		RemoteViews remoteViews = new RemoteViews(context.getPackageName(), R.layout.main);

		ComponentName componentName = new ComponentName(context, DoingWidget.class);

		appWidgetManager.updateAppWidget(componentName, remoteViews);
	}
}
</pre>

### main.xml

<pre>
LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical" 

    TextView
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="@string/app_name" 
        android:textColor="#ff0000"
        android:textSize="25sp"/

/LinearLayout
（为什么不是EditText，后面再讲）
</pre>

### appwidget_provider.xml

<pre>
!-- 指定该桌面组件的基本配置信息：
	minWidth：桌面小控件的最小宽度。
	minWidth：桌面小控件的最小高度。
	updatePeriodMillis：更新频率
	initialLayout：初始时显示的布局 --
appwidget-provider
	xmlns:android="http://schemas.android.com/apk/res/android"
	android:minWidth="150dip"
	android:minHeight="70dip"
	android:updatePeriodMillis="1000"
	android:initialLayout="@layout/main"/
</pre>

### AndroidManifest.xml

<pre>
manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.tobe"
    android:versionCode="1"
    android:versionName="1.0" 

    uses-sdk android:minSdkVersion="10" /

    application
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name" 
        
        receiver android:name=".DoingWidget"	
			android:label="@string/app_name"
			!-- 将该BroadcastReceiver当成桌面小控件 --
			intent-filter
				action android:name="android.appwidget.action.APPWIDGET_UPDATE" /
			/intent-filter
			!-- 指定桌面小控件的meta-data --
			meta-data android:name="android.appwidget.provider"
				android:resource="@xml/appwidget_provider"/
		/receiver
		
    /application

/manifest
</pre>

## 总结

其实代码写到这里已经很完整了（就是说可以运行了），但是我们在布局文件里用的只是TextView而不是设想中的EditText，原因在于RemoteViews并不支持EditText（大家试试就知道了），更详细的解释可以看这里http://www.360doc.com/content/10/0624/18/11192_35011927.shtml（因为难翻墙，就只找到这个了，讲的蛮好的）。因此这个程序实际上是没有完成的（只能显示文字或图片），也就是我写这个题目的原因，暂时我也还没找到解决办法，如果有人解决了的话最好通告一声，小弟感激不尽啊。

![](/images/DoingWidget.png)
