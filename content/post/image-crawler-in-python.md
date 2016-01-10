+++
date = "2014-03-17T08:35:31+08:00"
draft = true
title = "image crawler in python"

+++



## Implement 

1. Get the html content, urllib2.urlopen
2. Search the image url, r'&ltimg src="(.*?)" /&gt'
3. Download them, urllib.urlretrieve

## Code
<pre>
#!/usr/bin/env python                                                                                                                                                                                               
# -*- coding: utf-8 -*-                                                                                                                                                                                             

import urllib2
import urllib
import re

def download_images():
  page_number = 1
  image_number = 1

  while page_number <= 8:
    # "http://500px.com/search?exclude_nude=true&page=3&q=pikachu&type=photos"                                                                                                                                      
    page_url = "http://500px.com/search?exclude_nude=true&page=" + str(page_number) + "&q=pikachu&type=photos"
    html = urllib2.urlopen(page_url).read()

    image_reg_string = r'<img src="(.*?)" />'
    image_reg = re.compile(image_reg_string)                                                                                                                                                                        
    image_url_list = image_reg.findall(html)

    for image_url in image_url_list:
      file_name = str(image_number) + ".jpg"
      print "Download " + file_name
      urllib.urlretrieve(image_url, file_name)
      image_number += 1

    page_number += 1


if __name__ == "__main__":
  download_images()
</pre>

## Reference

* <http://blog.sina.com.cn/s/blog_7407815a0101d1ib.html>
* <http://500px.com/search?exclude_nude=true&page=1&q=pikachu&type=photos>
* <http://blog.csdn.net/idragonkid/article/details/21340413>