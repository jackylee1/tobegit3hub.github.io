+++
date = "2016-01-10T08:35:29+08:00"
draft = true
title = "crawl my website"

+++



<pre>
# -*- encoding -*-                                                        
import urllib2 
def main():
  print "Crawling..."
  for pageNumber in range(1,11):
    fileName = "post/"+str(pageNumber)+".html"   
    url = "http://www.chendihao.cn/page/"+str(pageNumber)
    downloadFile = open(fileName, "w")
    html = urllib2.urlopen(url).read()
    downloadFile.write(html)
    downloadFile.close()
    print "Download "+fileName    
  print "End..."
if __name__ == "__main__":
  main()
</pre>