+++
date = "2012-12-15T08:35:27+08:00"
draft = true
title = "original introduce not a top"

+++



## 简介

“不是陀螺”是Android平台下基于中国传统陀螺的休闲游戏，玩家通过手划屏幕模拟真实对陀螺的鞭打，从而使陀螺加速旋转和移动（不多说，以后再补充，至于名字的由来以后再说吧）。

##参考资料

（如果想知道游戏的实现或者看不懂什么SurfaceView的先看游戏编程的这一类书）
基本上我们能找到的2D游戏源代码的结构都是一样的，看一下Android游戏编程这一类书的实例就能有大概了解了，自己写确实有些问题没考虑到。所以这次重写了游戏框架，基本上是抄《Android编程典型实例与项目开发》的“Q版疯狂大炮”项目的，书里也有更详细的介绍。

## 设计模式

先要说这个，因为我在游戏框架里两次用到了工厂模式（分别是Environment包和SurfaceView包），这样写的话源文件是多了，但是为后期的拓展提供了很大很大的便利（我个人感觉这样架构是比较巧妙的）。如果不知道我在说什么，可以看一下《大话设计模式》等书，不然很难理解这种设计的思路。

## 游戏元素

暂时只有手划陀螺这种游戏模式，而游戏的元素（大家不要抓字眼，就是说游戏由几部份组成）只有两个：Top（放在Top包内）和Environment（放在Environment内）。解释一下，Top就是屏幕上的陀螺，我们这种模式只有一个陀螺，所以整个程序只有一个Top对象，简单吧。至于Environment指陀螺所处的环境，在这里可以设置难度和场景，玩过之前的Demo应该知道有什么“飓风模式”或者“暴雪模式”，它的原理就是通过改变Top对象的属性来增减游戏的难度，然后实现不同绘图函数实现不同的场景。然后，与Environment关联的Top就叫做DependentTop，毫无疑问是继承Top类的，因为前期的Top类与外界的耦合度不能太大所以保留下来了，因此，陀螺的很多属性和方法都放在Top.java，而实际上游戏中的陀螺是一个DependentTop对象。

## 包（package）结构

不同功能的类应该放在不同的包里，包名建议用网络域名（如www.google.com）的倒写，所以我写的包名都是com.gg开头的，没问题吧？一共5个包：device包放有关具体手机的信息，因为不同手机的屏幕尺寸什么的是不一样的，为了日后的兼容性而保留下来，现在只有Constant类，而且只有屏幕长宽两个属性。environment包放各种Environment（通过上面应该知道Environment是游戏的两个元素之一吧），从命名基本可以知道每个类的功能，而且这些文件的代码绝大部分是一样，只是参数不同，比较特殊的是EnvironmentFactory.java，就是所说的工厂类（想弄懂的看一下设计模式）。Top包放陀螺的类，就Top类和DependentTop类，前面也有介绍。utility包放各种工具类，这些东西不会直接出现在界面上，不过会被其他类用到，例如Top里面就有一个Circle对象来显示成圆盘。view包放各种界面和调用这些界面的Activity，也是用工厂模式，不同的SurfaceView注册到SurfaceViewFactory就可以直接用了。强调一下，比较重要的是Top类，包含了陀螺的旋转和碰撞等属性行为，还有GameSurfaceView类负责游戏进行界面的绘制，还有GameActivity类负责不同游戏状态下界面的切换。

## 补充

这个版本与我之前给大家的源代码比较大的区别是没有了login包和game包，因为之前是想以不同的界面分不同的包，也就是把登录的SurfaceView和Activity放一个包，游戏的放另一个包。后来看书发现一般游戏都只有一个Activity，再搭配多个SurfaceView，我看过几本书里游戏项目的源代码都是这样的，果断就改了。不过逻辑部分重点还是在Top类和GameSurfaceView类里面，所以不想斟酌全部代码而只要实现部分功能的可以不用管其他那么多的文件。

————–希望看完对整个项目有大致的了解—————