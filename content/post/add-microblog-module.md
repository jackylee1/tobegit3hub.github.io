+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "add microblog module"

+++



1 所谓微博，就是就是吐槽、宣泄、记录与感受嘛。写在Microblog里稀饭不影响博客质量啊 O(∩_∩)O哈哈~

2 要实现Microblog模块，首先要在index.php过滤掉Microblog分类的Post。只要一行代码。

<pre>
&lt?php if(in_category('9')) continue; ?&gt
</pre>

3 然后还要建一个Template来实现Microblog分类，只要将index.php复制，然后自己从数据库中拉去相应的Post即可，代码也不多。

<pre>
/ *
  * Template Name: Microblog Templat
  */
</pre>

<pre>
&lt?php
  $limit = get_option('posts_per_page');
  $paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
  query_posts('category_name=Microblog');
  wp_query->is_archive = true; $wp_query->is_home = false;
?&gt
</pre>