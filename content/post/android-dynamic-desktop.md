+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "android dynamic desktop"

+++



## 简介

参照动态桌面官方范例源代码 —— CubeWallpaper可以快速开发自己的动态桌面，但实际上一个完整的程序还需要其他的资源文件，在这里以准备用的BallWallpaper为例子贴出所有代码。

## 源文件（不需要Activity，只有一个BallWallpaper.java）

<pre>
package com.tobe;

import android.graphics.*;
import android.os.Handler;
import android.service.wallpaper.WallpaperService;
import android.view.MotionEvent;
import android.view.SurfaceHolder;

public class BallWallpaper extends WallpaperService {
	@Override
	public Engine onCreateEngine() {
		return new BallEngine();
	}

	class BallEngine extends Engine {
		private boolean isVisible;
		private float xTouch = -1;
		private float yTouch = -1;
		private float xBall = 15;
		private float yBall = 20;
		private Paint paint = new Paint();
		Handler mHandler = new Handler();
		private final Runnable drawTarget = new Runnable() {
			public void run() {
				draw();
			}
		};

		@Override
		public void onCreate(SurfaceHolder surfaceHolder) {
			super.onCreate(surfaceHolder);
			
			paint.setColor(0xffffffff);
			paint.setAntiAlias(true);
			paint.setStrokeWidth(2);
			paint.setStrokeCap(Paint.Cap.ROUND);
			paint.setStyle(Paint.Style.STROKE);

			setTouchEventsEnabled(true);
		}

		@Override
		public void onDestroy() {
			super.onDestroy();

			mHandler.removeCallbacks(drawTarget);
		}

		@Override
		public void onVisibilityChanged(boolean visible) {
			isVisible = visible;
			if (visible) {
				draw();
			} else {
				mHandler.removeCallbacks(drawTarget);
			}
		}

		@Override
		public void onOffsetsChanged(float xOffset, float yOffset, float xStep,
				float yStep, int xPixels, int yPixels) {
			draw();
		}
		

		@Override
		public void onTouchEvent(MotionEvent event) {
			if (event.getAction() == MotionEvent.ACTION_MOVE) {
				xTouch = event.getX();
				yTouch = event.getY();
			} else {
				xTouch = -1;
				yTouch = -1;
			}
			super.onTouchEvent(event);
		}

		private void logic(){
			
		}

		private void draw() {
			final SurfaceHolder holder = getSurfaceHolder();
			Canvas c = null;
			try {
				c = holder.lockCanvas();
				if (c != null) {
					c.save();
					c.drawColor(0xff000000);
			
					drawTouchPoint(c);
					c.drawCircle(xBall, yBall, 80, paint);
					c.restore();
				}
			} finally {
				if (c != null)
					holder.unlockCanvasAndPost(c);
			}
			mHandler.removeCallbacks(drawTarget);
			if (isVisible) {
				xBall += 15;
				yBall += 20;
				if (xBall > 320)
					xBall = 15;
				if (yBall > 400)
					yBall= 20;
				mHandler.postDelayed(drawTarget, 100);
			}
		}

		private void drawTouchPoint(Canvas c) {
			if (xTouch >= 0 && yTouch >= 0) {
				c.drawCircle(xTouch, yTouch, 40, paint);
			}
		}
		
	}
}
</pre>

## res文件（可以自己导入icon，还有xml文件夹下的ballwallpaper.xml）

<pre>
&lt?xml version="1.0" encoding="utf-8"?&gt
&ltwallpaper xmlns:android="http://schemas.android.com/apk/res/android"/&gt
&lt/xml&gt
</pre>

## 配置文件（修改AndroidManifest.xml）

<pre>
&ltservice android:label="@string/app_name"
  android:name=".BallWallpaper"
  android:permission="android.permission.BIND_WALLPAPER"&gt
    &ltintent-filter&gt
      &ltaction android:name="android.service.wallpaper.WallpaperService" /&gt
    &lt/intent-filter&gt
    &ltmeta-data android:name="android.service.wallpaper"
        android:resource="@xml/ballwallpaper" /&gt
&lt/service&gt
</pre>

## Done

![](/images/dynamic-desktop.jpg)