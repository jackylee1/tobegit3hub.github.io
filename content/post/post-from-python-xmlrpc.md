+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "post from python xmlrpc"

+++



Okay, this is posted by my app which is written in Python. Here is the source code.

(Remember to change with your username, password and active XML-RPC protocol for  your WordPress. Unfortunately it may not gonna work in Python3.3)

<pre><code>
import datetime, xmlrpclib

wp_url = "http://www.chendihao.cn/xmlrpc.php"
wp_username = "foo"
wp_password = "bar"
wp_blogid = ""

status_draft = 0
status_published = 1

server = xmlrpclib.ServerProxy(wp_url)

title = "Post from Python XML-RPC"
content = "pass"
date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2012-11-30 22:43", "%Y-%m-%d %H:%M"))
categories = ["Python"]
tags = []
data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
</code></pre>