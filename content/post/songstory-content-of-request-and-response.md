+++
date = "2016-01-10T08:35:29+08:00"
draft = true
title = "songstory content of request and response"

+++



## 请求

<pre>
请求方式: HTTP GET
请求参数，category_number, song_number
请求URL，”http://www.chendihao.cn/SongStoryServer/response.php?category_number=”+categoryNumber+”&song_number=”+songNumber
</pre>

## 响应

<pre>
如果存在返回JSON格式，{“is_exist”:false,”ss_url”:””}
如果不存在返回JSON格式，{“is_exist”:true,”ss_url”:”http:\/\/www.chendihao.cn\/SongStoryServer\/ss\/001.ss”}
</pre>