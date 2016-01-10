+++
date = "2014-10-06T08:35:32+08:00"
draft = true
title = "how to implement a web crawler zh"

+++



## 简单的网页爬虫

### 基本思路：
1. 获取所需抓取的网页
2. 分析网页源码提取所需抓取内容的规则
3. 根据规则写正则表达式过滤出内容
4. 保存内容

### 源代码：
<http://github.com/kiic-leung/learn-python/blob/master/spiders_pikachu.py>

### 例子：抓500px.com上的比卡丘图

#### （1）获取所需抓取的网页

在500px.com上搜索‘pikachu’，共有8页搜索结果。
> 第一页url：http://500px.com/search?exclude_nude=true&page=1&q=pikachu&type=photos
> 第二页url：http://500px.com/search?exclude_nude=true&page=2&q=pikachu&type=photos
> ……
> 第八页url：http://500px.com/search?exclude_nude=true&page=8&q=pikachu&type=photos

因此url的构成为：

    site_url = "http://500px.com/search?exclude_nude=true&page=" + str(page_number) + "&q=pikachu&type=photos"

#### （2）确定网页url后，需要用到urllib2组件来获取网页：

    import urllib2
    html = urllib2.urlopen(site_url).read()

> urllib2是python的一个获取url（Uniform Resource Locators，统一资源定址器）的模块。它用urlopen函数的形式提供了一个非常简洁的接口。它同时也提供了一个稍微复杂的接口来处理常见的状况-如基本的认证，cookies，代理，等等。这些都是由叫做opener和handler的对象来处理的。
>
> urllib2最简单的使用方式是调用urlopen方法，urllib2.urlopen(url[, data][, timeout]):
>
>     html = urllib2.urlopen(site_url).read()
>
> 调用urlopen函数对请求的url(Request对象)返回一个类文件对象（response对象），可以用.read()函数操作这个类文件对象。

#### （3）分析网页源码提取所需抓取内容的规则

图片的标签为：

    <img src='/uploads/default/4/662a817430089185.jpg'>

<img src='/uploads/default/4/662a817430089185.jpg'>

    <img src='/uploads/default/5/662a817430089185.jpg'>

<img src='/uploads/default/5/662a817430089185.jpg'>


#### （4）根据规则写正则表达式过滤出内容

    import re    # python通过re模块提供对正则表达式的支持。
    image_reg_string = r'src="(.*?\.jpg)" '
    img_reg = re.compile(image_reg_string) # 将正则表达式的字符串形式编译为一个Pattern实例
    image_list = re.findall(img_reg,html) # 以列表形式返回全部能匹配的子串

#### （5）下载图片

    import urllib
    for image_url in image_list: #遍历匹配结果列表
      urllib.urlretrieve(image_url,'picture_%s.jpg' %image_number) #urlretrieve直接将远程数据下载到本地

> urllib.urlretrieve(url[, filename[, reporthook[, data]]])
>
>参数说明：
> url：外部或者本地url
> filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）；
> reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度。
> data：指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。

