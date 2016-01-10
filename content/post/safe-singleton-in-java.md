+++
date = "2016-01-10T08:35:30+08:00"
draft = true
title = "safe singleton in java"

+++



## Singleton

* just People kiic = new People()
* always return instance

## Lazy initialization 

* if kiic == null than new
* but not safe

## Synchronized

* add synchronized to function
* it's low efficient

## Double-checked locking

* if kiic == null, then synchronized and if kiic == null
* reduce the synchronized object
* but the object may not finish initializing
* <http://blog.sina.com.cn/s/blog_75247c770100yxpb.html> points out the problem

## Safe lazy solution

* add volatile to limit the sequence 
* <http://www.infoq.com/cn/articles/double-checked-locking-with-delay-initialization> explain them

## Initialization on demand holder

* user inner class to hold the object

## Example

<pre><code>
  private volatile static Configuration conf = null;

  private FailoverUtil() {
  }

  public static Configuration getConf() {
    if (conf == null) {
      synchronized (conf) {
        if (conf == null) {
          conf = new Configuration();
        }
      }
    }
    return conf;
  }
</code></pre>