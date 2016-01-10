+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "simple rails project itidol zh"

+++



## 简介

[IT Idol](http://itidol.herokuapp.com/)是基于Rails部署在heroku的一个网站，它列举了IT界的一些偶像级人物，还有他们的贡献、名言，然后进行排序展示。这是一个非常简单的网站，可以说是Rails初学者的练手项目，如果你学习了Rails很多概念而不知道构建一个真正的项目，itidol也许可以帮到你。

## 步骤
1. 首先是使用rails的命令创建一个新的项目。
2. 然后生成你的model（如这里的idol和comment）、view和controller。
3. 接着创建一个StaticPage的controller，定义一个index或者home页面。
4. 借着就是使用[Bootstrap](http://getbootstrap.com/)库，调整你的Html布局和Css样式。
5. 然后使用[travis-ci](https://travis-ci.org/)做持续集成，提交.travis.yml文件。
6. 最后初始化[heroku](https://www.heroku.com/)应用，直接`git push heroku master`来部署。

## 源码

### idol.rb

<https://github.com/tobegit3hub/itidol/blob/master/app/models/idol.rb>

### comment.rb

<https://github.com/tobegit3hub/itidol/blob/master/app/models/comment.rb>

### static_page_controller.rb

<https://github.com/tobegit3hub/itidol/blob/master/app/controllers/static_page_controller.rb>

### home.html.erb

<https://github.com/tobegit3hub/itidol/blob/master/app/views/static_page/home.html.erb>

### routes.rb

<https://github.com/tobegit3hub/itidol/blob/master/config/routes.rb>
