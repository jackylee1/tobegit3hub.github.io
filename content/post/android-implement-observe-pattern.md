+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "android implement observe pattern"

+++



## Observer.java

<pre>
package cn.chendihao;

public abstract class Observer {

	public abstract void update(String string);
}
</pre>

## Subject.java

<pre>
package cn.chendihao;

import java.util.ArrayList;

public abstract class Subject {

	private ArrayList<Observer> observers = new ArrayList<Observer>();
	
	public void attachObserver(Observer observer){
		observers.add(observer);
	}
	
	public void detachObserver(Observer observer){
		observers.remove(observer);
	}
	
	public void notifyObservers(String string){
		for(int i=0; i<observers.size(); ++i){
			observers.get(i).update(string);
		}
	}
}
</pre>

## MainActivity.java

<pre>
package cn.chendihao.ui;

import java.util.ArrayList;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.RadioGroup.OnCheckedChangeListener;
import android.widget.TextView;
import cn.chendihao.R;
import cn.chendihao.R.layout;

public class MainActivity extends Activity {
	
	public ColorFrame colorFrame; // the first window
	public ListColorFrame listColorFrame; // the second window
	public ChangeColorFrame changeColorFrame; // the third window
	

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        colorFrame = new ColorFrame(this);
        listColorFrame = new ListColorFrame(this);
        changeColorFrame = new ChangeColorFrame(this);
        
        changeColorFrame.attachObserver(colorFrame);
        changeColorFrame.attachObserver(listColorFrame);

    }
}
</pre>

## ChangeColorFrame.java

<pre>
package cn.chendihao.ui;

import android.app.Activity;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.RadioGroup.OnCheckedChangeListener;
import cn.chendihao.R;
import cn.chendihao.Subject;

public class ChangeColorFrame extends Subject{
	
	public RadioGroup radioGroup;
	public RadioButton redButton;
	public RadioButton greenButton;
	public RadioButton blueButton;

	public ChangeColorFrame(Activity activity){
        radioGroup = (RadioGroup)activity.findViewById(R.id.colorGroup);
        redButton = (RadioButton)activity.findViewById(R.id.red);
        greenButton = (RadioButton)activity.findViewById(R.id.green);
        blueButton = (RadioButton)activity.findViewById(R.id.blue);
        
        
        radioGroup.setOnCheckedChangeListener(new OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                if(checkedId == redButton.getId()){
                	notifyObservers("Red");
                }else if(checkedId == greenButton.getId()){
                	notifyObservers("Green");
                }else if(checkedId == blueButton.getId()){
                	notifyObservers("Blue");
                }
            }
        });
	}
}
</pre>

## ColorFrame.java

<pre>
package cn.chendihao.ui;

import cn.chendihao.Observer;
import cn.chendihao.R;
import android.app.Activity;
import android.graphics.Color;
import android.widget.LinearLayout;
import android.widget.TextView;


public class ColorFrame extends Observer {
	
	public LinearLayout colorFrameLayout;
	public TextView colorName;
	
	
	public ColorFrame(Activity activity){
        colorFrameLayout = (LinearLayout)activity.findViewById(R.id.colorFrame);
        colorName = (TextView)activity.findViewById(R.id.colorName);
	}


	@Override
	public void update(String string) {
		if(string.equalsIgnoreCase("Red")){
        	colorName.setText("Red");
        	colorFrameLayout.setBackgroundColor(Color.rgb(255,0,0));
		}else if(string.equalsIgnoreCase("Green")){
        	colorName.setText("Green");
        	colorFrameLayout.setBackgroundColor(Color.rgb(0,255,0));
		}else if(string.equalsIgnoreCase("Blue")){
        	colorName.setText("Blue");
        	colorFrameLayout.setBackgroundColor(Color.rgb(0,0,255));
		}
		
	}
}
</pre>

## ListColorFrame.java

<pre>
package cn.chendihao.ui;

import java.util.ArrayList;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ListView;
import android.widget.TextView;
import cn.chendihao.Observer;
import cn.chendihao.R;

public class ListColorFrame extends Observer{
	
	public ArrayList<String> colorStrings = new ArrayList<String>();
	public ListView colorStringView;
	public BaseAdapter colorStringsAdapter;

	public ListColorFrame(final Activity activity){
		
		colorStringView = (ListView)activity.findViewById(R.id.colorList);
		
        colorStringsAdapter = new BaseAdapter(){

			@Override
			public int getCount() {
				return colorStrings.size();
			}

			@Override
			public Object getItem(int position) {
				return null;
			}

			@Override
			public long getItemId(int position) {
				return 0;
			}

			@Override
			public View getView(int position, View convertView, ViewGroup parent) {
				TextView colorStringView = new TextView(activity);
				colorStringView.setTextSize(20);
				colorStringView.setText(colorStrings.get(position));
				return colorStringView;
			}
        	
        };
        
        colorStringView.setAdapter(colorStringsAdapter);
	}

	@Override
	public void update(String string) {
		if(string.equalsIgnoreCase("Red")){
        	colorStrings.add("Red");
        	colorStringsAdapter.notifyDataSetChanged();
		}else if(string.equalsIgnoreCase("Green")){
        	colorStrings.add("Green");
        	colorStringsAdapter.notifyDataSetChanged();
		}else if(string.equalsIgnoreCase("Blue")){
        	colorStrings.add("Blue");
        	colorStringsAdapter.notifyDataSetChanged();
		}
		
	}
}
</pre>