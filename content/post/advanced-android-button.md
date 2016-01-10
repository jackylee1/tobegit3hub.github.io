+++
date = "2012-12-01T08:35:27+08:00"
draft = true
title = "advanced android button"

+++



小米实习回来以后，要判断一个App是由大学生开发的还是由企业团队来开发的就实在太简单了。看细节，像小米这样的公司已经有足够的资本去关注一个Button的二态或者三态，每一个切图都要切三份然后再去适配Android和iPhone，个人项目应该不会考虑吧。

所谓二态就是说Button在press和常规态时应使用不同颜色深度的切图，这样可以给用户quick response，以表明未选中、选中或者撤销。因为Android开发使用MVC模式，所以要实现二态很简单，代码如下。

<pre><code>
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android" >
    <item android:state_pressed="true" android:drawable="@drawable/button_pressed"/>
    <item android:drawable="@drawable/button_normal"/>
</selector>
</code></pre>

三态甚至是四态同样简单。

<pre><code>
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android" >
    <item android:state_selected="true" android:drawable="@drawable/button_pressed" />
    <item android:state_focused="true" android:drawable="@drawable/button_pressed" />
    <item android:state_pressed="true" android:drawable="@drawable/button_pressed" />
    <item android:drawable="@drawable/button_normal"/>
</selector>
</code></pre>
