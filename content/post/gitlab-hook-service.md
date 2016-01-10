+++
date = "2014-11-30T08:35:32+08:00"
draft = true
title = "gitlab hook service"

+++



## Hook服务

钩子服务，听起来很复杂，其实任何人都可以掌握并且用上。

什么时候需要用Hook呢？其实这是Github或者Gitlab提供的一项服务，允许我们接收Git事件做相应的操作。例如我们使用[mkdocs](https://github.com/tomchristie/mkdocs)生成文档网站，因为源文件是Markdown文件，每次添加新的文档需要重新`mkdocs build`才能生成新的文档页，手动或定期转显然不合理，使用Hook就可以很好解决这个问题。

## 实现Web服务

Gitlab提供一个Web Hook接口，只要在项目settings页填上一个IP地址和端口，每次Push、Pull-request、issue都会向这个服务器地址发送JSON请求。我们可以使用任何编程语言，实现一个Web Service，接收这个JSON请求并做相应处理就可以了。

于是我用Go和原生的http库实现了一个，代码在<https://github.com/tobegit3hub/gitlab_hook_service>。每次有代码提交，它都会在本地执行`git pull`以获得最新代码，你只需要将这个服务端IP和端口填到Gitlab的配置就可以了。

