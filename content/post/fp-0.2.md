+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "fp 0.2"

+++



只有一个Activity，使用自己的SurfaceView生成3*4布局（多一行可选高八度或者低八度），onTouchEvent来响应多指触控，按屏幕长宽来布局所以放在Constant中。

## MainActivity.java

<pre>
package cn.chendihao;

import android.app.Activity;
import android.content.pm.ActivityInfo;
import android.media.AudioManager;
import android.media.SoundPool;
import android.os.Bundle;
import android.os.Vibrator;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Display;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;

public class MainActivity extends Activity{
	
	private Activity mainActivity;
	//private View mainView;

	public MainActivity(){
		mainActivity = this;
	}
	
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        //requestWindowFeature(Window.FEATURE_NO_TITLE); // 隐藏标题栏
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, // 设置全屏
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE); // 设置横屏
        
        Display display = getWindowManager().getDefaultDisplay();
        Constant.SCREEN_WIDTH = display.getWidth();
        Constant.SCREEN_HEIGHT = display.getHeight();

        setContentView(new MainView(this));
    }
	
}
</pre>

## MainView.java

<pre>
package cn.chendihao;

import android.app.Activity;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.media.AudioManager;
import android.media.SoundPool;
import android.os.Vibrator;
import android.view.MotionEvent;
import android.view.SurfaceHolder;
import android.view.SurfaceHolder.Callback;
import android.view.SurfaceView;

public class MainView extends SurfaceView implements Callback, Runnable{
	
	private Activity mainActivity;
	
	private SoundPool soundPool;
	
	private Vibrator vibrator;
	
	private int offset = 0;
	
	private int sound1;
	private int sound2;
	private int sound3;
	private int sound4;
	private int sound5;
	private int sound6;
	private int sound7;
	
	private int sound1m;
	private int sound2m;
	private int sound3m;
	private int sound4m;
	private int sound5m;
	private int sound6m;
	private int sound7m;
	
	private int sound1p;
	private int sound2p;
	private int sound3p;
	private int sound4p;
	private int sound5p;
	private int sound6p;
	private int sound7p;
		
	private SurfaceHolder surfaceHolder;
	private Canvas canvas;
	private boolean isRunning = false;
	

	public MainView(Context context) {
		super(context);
		
		mainActivity = (Activity)context;
		
        vibrator = (Vibrator) mainActivity.getSystemService(mainActivity.VIBRATOR_SERVICE);    
        
        soundPool = new SoundPool(88, AudioManager.STREAM_MUSIC, 5); //STREAM_SYSTEM doesn't work for MiOne

        sound1m = soundPool.load(mainActivity, R.raw.m048, 1);
        sound2m = soundPool.load(mainActivity, R.raw.m050, 1);
        sound3m = soundPool.load(mainActivity, R.raw.m052, 1);
        sound4m = soundPool.load(mainActivity, R.raw.m053, 1);
        sound5m = soundPool.load(mainActivity, R.raw.m055, 1);
        sound6m = soundPool.load(mainActivity, R.raw.m057, 1);
        sound7m = soundPool.load(mainActivity, R.raw.m059, 1);
        
        sound1 = soundPool.load(mainActivity, R.raw.m060, 1);
        sound2 = soundPool.load(mainActivity, R.raw.m062, 1);
        sound3 = soundPool.load(mainActivity, R.raw.m064, 1);
        sound4 = soundPool.load(mainActivity, R.raw.m065, 1);
        sound5 = soundPool.load(mainActivity, R.raw.m067, 1);
        sound6 = soundPool.load(mainActivity, R.raw.m069, 1);
        sound7 = soundPool.load(mainActivity, R.raw.m071, 1);
        
        sound1p = soundPool.load(mainActivity, R.raw.m072, 1);
        sound2p = soundPool.load(mainActivity, R.raw.m074, 1);
        sound3p = soundPool.load(mainActivity, R.raw.m076, 1);
        sound4p = soundPool.load(mainActivity, R.raw.m077, 1);
        sound5p = soundPool.load(mainActivity, R.raw.m079, 1);
        sound6p = soundPool.load(mainActivity, R.raw.m081, 1);
        sound7p = soundPool.load(mainActivity, R.raw.m083, 1);
           
		surfaceHolder = this.getHolder();
		surfaceHolder.addCallback(this);
	}

	@Override
	public void surfaceChanged(SurfaceHolder holder, int format, int width,
			int height) {
		
	}

	@Override
	public void surfaceCreated(SurfaceHolder holder) {
		new Thread(this).start();
		isRunning = true;
	}

	@Override
	public void surfaceDestroyed(SurfaceHolder holder) {
		isRunning = false;
	}

	@Override
	public void run() {
		while(isRunning){
			
			drawAll();
			
			try{
				Thread.sleep(100);
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	
	private void drawAll(){
		
		canvas = surfaceHolder.lockCanvas();
		
		Paint paint = new Paint();
		Paint textPaint = new Paint();
		textPaint.setColor(Color.BLACK);
		textPaint.setTextSize(20);
		
		canvas.drawColor(Color.TRANSPARENT);	
		
		paint.setColor(Color.RED);
		canvas.drawRect(0*Constant.SCREEN_WIDTH/4, 0*Constant.SCREEN_HEIGHT/3, 1*Constant.SCREEN_WIDTH/4, 1*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("高八度", 1*Constant.SCREEN_WIDTH/8, 1*Constant.SCREEN_HEIGHT/6, textPaint);
		
		paint.setColor(Color.GREEN);
		canvas.drawRect(0*Constant.SCREEN_WIDTH/4, 1*Constant.SCREEN_HEIGHT/3, 1*Constant.SCREEN_WIDTH/4, 2*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("中央C", 1*Constant.SCREEN_WIDTH/8, 3*Constant.SCREEN_HEIGHT/6, textPaint);		
		
		paint.setColor(Color.BLUE);
		canvas.drawRect(0*Constant.SCREEN_WIDTH/4, 2*Constant.SCREEN_HEIGHT/3, 1*Constant.SCREEN_WIDTH/4, 3*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("低八度", 1*Constant.SCREEN_WIDTH/8, 5*Constant.SCREEN_HEIGHT/6, textPaint);
		
		//7,8,9 layout
		paint.setColor(Color.GRAY);
		canvas.drawRect(1*Constant.SCREEN_WIDTH/4, 0*Constant.SCREEN_HEIGHT/3, 2*Constant.SCREEN_WIDTH/4, 1*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("7", 3*Constant.SCREEN_WIDTH/8, 1*Constant.SCREEN_HEIGHT/6, textPaint);
		
		//4,5,6 layout
		paint.setColor(Color.GRAY);
		canvas.drawRect(1*Constant.SCREEN_WIDTH/4, 1*Constant.SCREEN_HEIGHT/3, 2*Constant.SCREEN_WIDTH/4, 2*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("4", 3*Constant.SCREEN_WIDTH/8, 3*Constant.SCREEN_HEIGHT/6, textPaint);
		
		paint.setColor(Color.GRAY);
		canvas.drawRect(2*Constant.SCREEN_WIDTH/4, 1*Constant.SCREEN_HEIGHT/3, 3*Constant.SCREEN_WIDTH/4, 2*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("5", 5*Constant.SCREEN_WIDTH/8, 3*Constant.SCREEN_HEIGHT/6, textPaint);		
		
		paint.setColor(Color.GRAY);
		canvas.drawRect(3*Constant.SCREEN_WIDTH/4, 1*Constant.SCREEN_HEIGHT/3, 4*Constant.SCREEN_WIDTH/4, 2*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("6", 7*Constant.SCREEN_WIDTH/8, 3*Constant.SCREEN_HEIGHT/6, textPaint);
				
		//1,2,3 layout
		paint.setColor(Color.GRAY);
		canvas.drawRect(1*Constant.SCREEN_WIDTH/4, 2*Constant.SCREEN_HEIGHT/3, 2*Constant.SCREEN_WIDTH/4, 3*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("1", 3*Constant.SCREEN_WIDTH/8, 5*Constant.SCREEN_HEIGHT/6, textPaint);
		
		paint.setColor(Color.GRAY);
		canvas.drawRect(2*Constant.SCREEN_WIDTH/4, 2*Constant.SCREEN_HEIGHT/3, 3*Constant.SCREEN_WIDTH/4, 3*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("2", 5*Constant.SCREEN_WIDTH/8, 5*Constant.SCREEN_HEIGHT/6, textPaint);		
		
		paint.setColor(Color.GRAY);
		canvas.drawRect(3*Constant.SCREEN_WIDTH/4, 2*Constant.SCREEN_HEIGHT/3, 4*Constant.SCREEN_WIDTH/4, 3*Constant.SCREEN_HEIGHT/3, paint);
		canvas.drawText("3", 7*Constant.SCREEN_WIDTH/8, 5*Constant.SCREEN_HEIGHT/6, textPaint);
		
		surfaceHolder.unlockCanvasAndPost(canvas);
	}

	@Override
	public boolean onTouchEvent(MotionEvent e) {

		int x = (int) e.getX(e.getActionIndex());
		int y = (int) e.getY(e.getActionIndex());

		switch(e.getAction()){
		case MotionEvent.ACTION_DOWN:
		case MotionEvent.ACTION_POINTER_1_DOWN:
		case MotionEvent.ACTION_POINTER_2_DOWN:
		case MotionEvent.ACTION_POINTER_3_DOWN:
		case MotionEvent.ACTION_POINTER_3_DOWN+256:
		//case MotionEvent.ACTION_POINTER_3_DOWN+256*2:
		//case MotionEvent.ACTION_POINTER_3_DOWN+256*3:
		//case MotionEvent.ACTION_POINTER_3_DOWN+256*4:
		//case MotionEvent.ACTION_POINTER_3_DOWN+256*5:
		//case MotionEvent.ACTION_POINTER_3_DOWN+256*6:
		//case MotionEvent.ACTION_POINTER_3_DOWN+256*7:
		//	updatePressedInfo(e);
			onDown(x, y);
			break;
		//case MotionEvent.ACTION_MOVE:
		//	updatePressedInfo(e);
		//	onMove(ax,ay,e.getPressure(e.getActionIndex()));
		//	break;
		case MotionEvent.ACTION_UP:
		case MotionEvent.ACTION_POINTER_1_UP:
		case MotionEvent.ACTION_POINTER_2_UP:
		case MotionEvent.ACTION_POINTER_3_UP:
		case MotionEvent.ACTION_POINTER_3_UP+256:
		case MotionEvent.ACTION_POINTER_3_UP+256*2:
		case MotionEvent.ACTION_POINTER_3_UP+256*3:
		case MotionEvent.ACTION_POINTER_3_UP+256*4:
		case MotionEvent.ACTION_POINTER_3_UP+256*5:
		case MotionEvent.ACTION_POINTER_3_UP+256*6:
		case MotionEvent.ACTION_POINTER_3_UP+256*7:
		//	updatePressedInfo(e);
		//	onUp(ax,ay);
			break;
		}
		return(true);
	}
	
	private void onUp(double x, double y){
		
	}
	
	private void onDown(double x, double y){
		if(x/Constant.SCREEN_WIDTH>0.0/4 && x/Constant.SCREEN_WIDTH<1.0/4 && y/Constant.SCREEN_HEIGHT>0.0/3 && y/Constant.SCREEN_HEIGHT<1.0/3){
			//高八度
			offset = 7;
		}else if(x/Constant.SCREEN_WIDTH>0.0/4 && x/Constant.SCREEN_WIDTH<1.0/4 && y/Constant.SCREEN_HEIGHT>1.0/3 && y/Constant.SCREEN_HEIGHT<2.0/3){
			//中央C
			offset = 0;
		}else if(x/Constant.SCREEN_WIDTH>0.0/4 && x/Constant.SCREEN_WIDTH<1.0/4 && y/Constant.SCREEN_HEIGHT>2.0/3 && y/Constant.SCREEN_HEIGHT<3.0/3){
			//低八度
			offset = -7;
		}else if(x/Constant.SCREEN_WIDTH>1.0/4 && x/Constant.SCREEN_WIDTH<2.0/4 && y/Constant.SCREEN_HEIGHT>2.0/3 && y/Constant.SCREEN_HEIGHT<3.0/3){
			//1
			vibrator.vibrate(100);
			soundPool.play(sound1+offset, 1, 1, 0, 0, 1);
		}else if(x/Constant.SCREEN_WIDTH>2.0/4 && x/Constant.SCREEN_WIDTH<3.0/4 && y/Constant.SCREEN_HEIGHT>2.0/3 && y/Constant.SCREEN_HEIGHT<3.0/3){
			//2
			vibrator.vibrate(100);
			soundPool.play(sound2+offset, 1, 1, 0, 0, 1);			
		}else if(x/Constant.SCREEN_WIDTH>3.0/4 && x/Constant.SCREEN_WIDTH<4.0/4 && y/Constant.SCREEN_HEIGHT>2.0/3 && y/Constant.SCREEN_HEIGHT<3.0/3){
			//3
			vibrator.vibrate(100);
			soundPool.play(sound3+offset, 1, 1, 0, 0, 1);
		}else if(x/Constant.SCREEN_WIDTH>1.0/4 && x/Constant.SCREEN_WIDTH<2.0/4 && y/Constant.SCREEN_HEIGHT>1.0/3 && y/Constant.SCREEN_HEIGHT<2.0/3){
			//4
			vibrator.vibrate(100);
			soundPool.play(sound4+offset, 1, 1, 0, 0, 1);
		}else if(x/Constant.SCREEN_WIDTH>2.0/4 && x/Constant.SCREEN_WIDTH<3.0/4 && y/Constant.SCREEN_HEIGHT>1.0/3 && y/Constant.SCREEN_HEIGHT<2.0/3){
			//5
			vibrator.vibrate(100);
			soundPool.play(sound5+offset, 1, 1, 0, 0, 1);
		}else if(x/Constant.SCREEN_WIDTH>3.0/4 && x/Constant.SCREEN_WIDTH<4.0/4 && y/Constant.SCREEN_HEIGHT>1.0/3 && y/Constant.SCREEN_HEIGHT<2.0/3){
			//6
			vibrator.vibrate(100);
			soundPool.play(sound6+offset, 1, 1, 0, 0, 1);
		}else if(x/Constant.SCREEN_WIDTH>1.0/4 && x/Constant.SCREEN_WIDTH<2.0/4 && y/Constant.SCREEN_HEIGHT>0.0/3 && y/Constant.SCREEN_HEIGHT<1.0/3){
			//7
			vibrator.vibrate(100);
			soundPool.play(sound7+offset, 1, 1, 0, 0, 1);
		}
	}
}
</pre>

## Constant.java

<pre>
package cn.chendihao;

public class Constant {

	public static int SCREEN_WIDTH = 0;
	public static int SCREEN_HEIGHT = 0;
}
</pre>

## 记得补AndroidManifest.xml

android.permission.VIBRATE

## 还需要导入m020.mid ~ m108.mid

![](/images/FP0.2.png)