+++
date = "2012-11-29T08:35:27+08:00"
draft = true
title = "write a website like this"

+++



Web2.0来了，拥有自己的个人网站仍然是一件很Geek的事。要开发这样的个人博客也不难，我来介绍一下具体流程：

1. 首先要有属于自己的服务器，我已搬家到衡天主机的美国加州西海岸机房。自己搭服务器是不现实的，购买空间时要注意中国的网络访问情况，一般国外空间比较便宜但在大陆访问不稳定。
2. 然后注册自己的域名，chendihao.cn是在新网购买的还可以，成功的话可以在http://cnnic.cn/查询到。现在购买与姓名强相关的cn域名比较优惠。注意了，域名和空间都是有期限的，必须续费才能用。
3. 既然有了服务器，我们也可以拿它来当FTP传文件，但更多的还是拿来写博客网站，可以自己用PHP实现，我选择WordPress。WordPress is a free and open sourceblogging tool and a content management system (CMS) based on PHPand MySQL. 也就是说不写代码也可以实现自己的博客系统了，赞。
4. 接着介绍安装WordPress，参考http://wiki.lanbing.me/45.shtml就好了。补充说明一下，安装WordPress需要提前创建一个的MySQL数据库和数据库用户，如果自动生成wp-config.php失败则手动拷贝代码然后FTP上去就可以了。
5. 这就是你们看到如此简洁的网页了，选择WordPress最大的好处就在于其扩展性，所以下一步就是自己写Theme和Plug-in啦，用PHP（其实不写也可以，网上有很多不错的主题和插件了）。

网上早有很多教程供参考，这只是我的个人实践，感谢<www.jiajunlo.com>的亲身指导。据说现在IT企业招人还要考察个人博客的运维时间，这同时也是一份很好的简历嘛。

目前个人博客从自己买的WordPress迁移到Github Page，可以直接`ack`查内容，太赞了！