+++
date = "2016-01-10T08:35:30+08:00"
draft = true
title = "research of web development"

+++



因为写了几个Python脚本，想集成web界面做个自动化工具，于是考虑用Python写个简单的页面，开始挑选web framework。原来Python不像PHP是针对web开发而设计的，所以写网站还是需要用到框架，这个其实也可以自己做，但是看到Django那一坨url、template、orm和admin就没兴趣了。

主流框架就是Django，文档最多（其实就是官方文档写得好），看了一下想写个网页还是挺麻烦的，利用框架将url、orm等东西都配置了，所以写起来麻烦，而且template language也很难看啊，一句话就是太重了。于是找轻量级的webpy，好像语法也是有点特异，这个增加学习成本啊，而且中大型的还是要用Django啊。还有豆瓣的“堂吉诃德”模块化便于拓展，不适用我这个超小型子项目。

以前是做过PHP的，而且SongStoryServer就是直接用PHP，SongStoryAdmin其实也可以，调用一下Python脚本或者直接用PHP重写即可。顾虑就是PHP太容易入门了吧，上网看了一下说连function都可以不会直接if-else也可以写个网站，而且没有package管理是硬伤。很多人反映quick and dirty，大项目应该少用吧，不过还是很感激它秒现了SongStoryServer的。

大二觉得J2EE是未来，而且刚好淘宝就是从PHP过渡到Java的，到现在小米Java也是这样用。后来逐渐明白PHP真的是为Web开发而生，也有存在的道理。不考虑用Java来做的原因，“代码太多了”。

于是转向一直想学的Ruby，学过Python的我觉得Python真是好，但是传说学过Python再学Ruby的最终都转为Ruby。Python的好处在于quick and clean，SongStoryWriteJson和SongStoryCreateSs都是用Python写的脚本，以后很多的Bash都可以直接用Python取代，Ruby应该也类似的general perpose。于是就有了Ruby on Rails这个选择，不过学习周期应该有点长，这么小一个东西这周搞不掂了。有人说想找工作学PHP，高效的学Python，想喜欢编程的学Ruby，所以Ruby时必学的，就像学过Vim还是必须学Emacs的，据说Martz就是看过Emacs才激发他创作Ruby的。

咦想了一下，这么小的项目可以自己写哦，用Ruby元编程设计自己的语言，用它的类库或者自己重写实现Server，可以吧。
