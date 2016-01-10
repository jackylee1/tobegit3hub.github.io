+++
date = "2013-02-23T08:35:28+08:00"
draft = true
title = "android preference"

+++



先提出问题，Android的设置界面为PreferenceActivity，其中的ListPreference选择后是没有显示结果的，然而大部分软件的设置界面都在summary那里显示了（米吧就是）。可恨的是Google没有提供相应回调函数接口，真的就要自己去实现跟新。

![](/images/preference-activity.png)


## SettingActivity.java

<pre>
package cn.chendihao;

import android.app.Activity;
import android.app.KeyguardManager;
import android.app.KeyguardManager.KeyguardLock;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences.OnSharedPreferenceChangeListener;
import android.os.Bundle;
import android.os.Handler;
import android.preference.Preference;
import android.preference.Preference.OnPreferenceChangeListener;
import android.preference.Preference.OnPreferenceClickListener;
import android.preference.PreferenceActivity;
import android.preference.PreferenceScreen;
import android.widget.Toast;

public class SettingActivity extends PreferenceActivity implements OnPreferenceChangeListener{
	
	private final Handler mHandler = new Handler();
	
	private BroadcastReceiver screenOnReceiver = new ScreenOnReceiver();
	
    public static final String KEY_AUTORUN = &quot;key_autorun&quot;;
    public static final String KEY_SHOW_TIME = &quot;key_show_time&quot;;
    public static final String KEY_SHOW_CONTENT = &quot;key_show_content&quot;;
    
    private Preference autorunPreference;
    private Preference showTimePreference;
    private Preference showContentPreference;
    
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
       
        addPreferencesFromResource(R.xml.preference);

        autorunPreference = findPreference(KEY_AUTORUN);
        showTimePreference = findPreference(KEY_SHOW_TIME);
        showContentPreference = findPreference(KEY_SHOW_CONTENT);

        showTimePreference.setSummary(showTimePreference.getSharedPreferences().getString(KEY_SHOW_TIME, &quot;&quot;));
        showContentPreference.setSummary(showContentPreference.getSharedPreferences().getString(KEY_SHOW_CONTENT, &quot;&quot;));
        
        autorunPreference.setOnPreferenceChangeListener(this);
        showTimePreference.setOnPreferenceChangeListener(this);
        showContentPreference.setOnPreferenceChangeListener(this);
    }

	@Override
	public boolean onPreferenceChange(final Preference arg0, Object arg1) {
	
		final String key = arg0.getKey();
		
		if(key.equals(KEY_AUTORUN) || key.equals(KEY_SHOW_TIME) || key.equals(KEY_SHOW_CONTENT)){
		
	        //希望250ms内newValue会被写进去。
	        mHandler.postDelayed(new Runnable() {
	
	            @Override
	            public void run() {
	            	if(key.equals(KEY_AUTORUN)){
	            		
	            		if(arg0.getSharedPreferences().getBoolean(KEY_AUTORUN, false)){
		    	        	IntentFilter filter = new IntentFilter(Intent.ACTION_SCREEN_ON); 
		    	        	//filter.addAction(&quot;android.intent.action.SCREEN_OFF&quot;); 
		    	        	registerReceiver(screenOnReceiver, filter); 

	            		}else{
	            			unregisterReceiver(screenOnReceiver);
	            		}

	            	}else if(key.equals(KEY_SHOW_TIME)){
	        	        showTimePreference.setSummary(arg0.getSharedPreferences().getString(KEY_SHOW_TIME, &quot;&quot;));
	        		}else if(key.equals(KEY_SHOW_CONTENT)){
	        			showContentPreference.setSummary(arg0.getSharedPreferences().getString(KEY_SHOW_CONTENT, &quot;&quot;));
	        		}
	            }
	        }, 250);
		}
        
        return true;        
	}
	
  @Override
  public boolean onPreferenceTreeClick(PreferenceScreen preferenceScreen, Preference preference) {

      return false;
  }
    
}
</pre>

补充一点，onPreferenceTreeClick(), onPreferenceChange()和onPreferenceClick()都是一样的，在点Perference时立即回调，这时新值未写入，设置的summary也是旧的（所以要点两次才可以嘛）。Google就不提供设置后的回调函数，气人啊！！