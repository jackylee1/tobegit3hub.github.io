+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "fp 0.1"

+++



只有一个Activity，使用xml文件生成3*3布局，onclick时使用SoundPool发声（生成020～108的MIDI文件）。

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
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;

public class MainActivity extends Activity implements OnClickListener{
	
	private Activity mainActivity;
	//private View mainView;
	
	private SoundPool soundPool;
	private Vibrator vibrator;
	
	private int sound1;
	private int sound2;
	private int sound3;
	private int sound4;
	private int sound5;
	private int sound6;
	private int sound7;
		
	private Button oneButton;
	private Button twoButton;
	private Button threeButton;
	private Button fourButton;
	private Button fiveButton;
	private Button sixButton;
	private Button sevenButton;
	private Button eightButton;
	private Button nineButton;

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
        
        setContentView(R.layout.main);
        
        vibrator = (Vibrator) getSystemService(VIBRATOR_SERVICE);    
        
        soundPool = new SoundPool(88, AudioManager.STREAM_MUSIC, 5); //STREAM_SYSTEM doesn't work for MiOne
        sound1 = soundPool.load(this, R.raw.m060, 1);
        sound2 = soundPool.load(this, R.raw.m062, 1);
        sound3 = soundPool.load(this, R.raw.m064, 1);
        sound4 = soundPool.load(this, R.raw.m065, 1);
        sound5 = soundPool.load(this, R.raw.m067, 1);
        sound6 = soundPool.load(this, R.raw.m069, 1);
        sound7 = soundPool.load(this, R.raw.m071, 1);
        
        oneButton = (Button) findViewById(R.id.one);
        twoButton = (Button) findViewById(R.id.two);
        threeButton = (Button) findViewById(R.id.three);
        fourButton = (Button) findViewById(R.id.four);
        fiveButton = (Button) findViewById(R.id.five);
        sixButton = (Button) findViewById(R.id.six);
        sevenButton = (Button) findViewById(R.id.seven);
        eightButton = (Button) findViewById(R.id.eight);
        nineButton = (Button) findViewById(R.id.nine);
        
        oneButton.setOnClickListener(this);
        twoButton.setOnClickListener(this);
        threeButton.setOnClickListener(this);
        fourButton.setOnClickListener(this);
        fiveButton.setOnClickListener(this);
        sixButton.setOnClickListener(this);
        sevenButton.setOnClickListener(this);
        
        eightButton.setClickable(false);
        nineButton.setClickable(false);
    }


	@Override
	public void onClick(View v) {
		
		vibrator.vibrate(100);
		
		if(v.getId()==R.id.one){
			soundPool.play(sound1, 1, 1, 0, 0, 1);
		}else if(v.getId()==R.id.two){
			soundPool.play(sound2, 1, 1, 0, 0, 1);
		}else if(v.getId()==R.id.three){
			soundPool.play(sound3, 1, 1, 0, 0, 1);
		}else if(v.getId()==R.id.four){
			soundPool.play(sound4, 1, 1, 0, 0, 1);
		}else if(v.getId()==R.id.five){
			soundPool.play(sound5, 1, 1, 0, 0, 1);
		}else if(v.getId()==R.id.six){
			soundPool.play(sound6, 1, 1, 0, 0, 1);
		}else if(v.getId()==R.id.seven){
			soundPool.play(sound7, 1, 1, 0, 0, 1);
		}
	}
	
}
</pre>

<h2>记得补AndroidManifest.xml</h2>

android.permission.VIBRATE

<h2>还需要导入m020.mid ~ m108.mid</h2>

![](/images/FP0.1.png)