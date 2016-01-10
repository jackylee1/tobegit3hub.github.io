+++
date = "2016-01-10T08:35:29+08:00"
draft = true
title = "kiiccalll"

+++



## <https://github.com/tobegit3hub/KiicCall>

## 新建Android项目，并作以下调整
1. 加入打电话功能代码，同时添加directly call权限
2. 加入自定义图片的Toast，并显示
3. 一开始就finish掉自身Activity

## 源代码  

<pre>
package cn.chendihao.kiiccall;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

public class MainActivity extends Activity {
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    
        this.finish();
    
    
        ImageView imageView = new ImageView(this);
        imageView.setImageResource(R.drawable.heart);
    
        Toast toast = new Toast(this);
        toast.setView(imageView);
        toast.setDuration(Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0); 
        toast.show();
    
    
        String tobeNumber = "626796";  //637104
        Intent intent = new Intent(Intent.ACTION_CALL);
        intent.setData(Uri.parse("tel:"+tobeNumber));
        startActivity(intent);

    }   
 }
</pre>
