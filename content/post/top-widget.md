+++
date = "2012-12-31T08:35:27+08:00"
draft = true
title = "top widget"

+++



## 简介

TopWidget是“不是陀螺”系列产品中的Widget，纯粹是用来熟悉Android Widget代码的编写，如图右上角会持续转动的陀螺图形。

![](/images/TopWidget.jpg)

## 实现

1.1完全基于之前所写的DoingWidget，详见自己动手写Android Widget —— DoingWidget（未完成版）。
1.2加入Timer动态更换不同的图片。

## 源代码（不同于DoingWidget的）

### 2.1.TopWidget.java（代替DoingWidget.java）

<pre>
package com.tobe;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.ComponentName;
import android.content.Context;
import android.os.Handler;
import android.os.Message;
import android.widget.RemoteViews;

public class TopWidget extends AppWidgetProvider {
	private Timer timer = new Timer();
	private AppWidgetManager appWidgetManager;
	private Context context;
	private int indexImage = 0;

	private int[] idTopImages = new int[] { R.drawable.top1, R.drawable.top2,
			R.drawable.top3, R.drawable.top4, R.drawable.top5, R.drawable.top6};

	@Override
	public void onUpdate(Context context, AppWidgetManager appWidgetManager,
			int[] appWidgetIds) {
		this.appWidgetManager = appWidgetManager;
		this.context = context;
		timer = new Timer();

		timer.schedule(new TimerTask() {
			public void run() {
				handler.sendEmptyMessage(0x123);
			}
		}, 0, 200);
	}

	private Handler handler = new Handler() {
		public void handleMessage(Message msg) {
			if (msg.what == 0x123) {
				RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.main);
				
				views.setImageViewResource(R.id.idImageView, idTopImages[indexImage]);
				if(indexImage>=5) {
					indexImage = 0;
				}else{
					indexImage++;
				}
				
				ComponentName componentName = new ComponentName(context, TopWidget.class);
				
				appWidgetManager.updateAppWidget(componentName, views);
			}
			super.handleMessage(msg);
		}
	};
}
</pre>

### main.xml（将TextView改为ImageView而已）

<pre>
LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical" 

    ImageView android:id="@+id/idImageView"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent" 
        /

/LinearLayout
</pre>

### appwidget_provider.xml（将长宽改小成为正方形而已）

<pre>
!-- 指定该桌面组件的基本配置信息：
	minWidth：桌面小控件的最小宽度。
	minWidth：桌面小控件的最小高度。
	updatePeriodMillis：更新频率
	initialLayout：初始时显示的布局 --
appwidget-provider
	xmlns:android="http://schemas.android.com/apk/res/android"
	android:minWidth="60dip"
	android:minHeight="60dip"
	android:updatePeriodMillis="1000"
	android:initialLayout="@layout/main"/
</pre>

## 总结

用Timer定时更换图片基本实现了动画，里面有一些参数可以调：例如timer.schedule里面的200就是刷新屏率，设为100会更平滑，不过如果放太多控件的话会造成Launcher崩溃；还有appwidget_provider.xml中长宽的修改不出意外可以调整Widget在真机中所占的格子数。至于能不能进行交互操作估计比较难，建议最好也不要，更多学习内容还是建议去http://www.360doc.com/content/10/0624/18/11192_35011927.shtml看看。