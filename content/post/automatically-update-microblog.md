+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "automatically update microblog"

+++



## Oauth

这代码亲测无效（原理是Oauth认证，估计是改了API）。

<pre>
function post_to_sina_weibo($post_ID) {
  if( wp_is_post_revision($post_ID) ) return;

  // 将 abc 替换成你的新浪微博登陆名
  $username = "abc"
  // 将 123 替换成你的新浪微博密码
  $password = "123";

  $get_post_info = get_post($post_ID);
 
  if ( $get_post_info->post_status == 'publish' && $_POST['original_post_status'] != 'publish' ) {
    $status = strip_tags( $_POST['post_title'] ) . ' ' . urlencode( get_permalink($post_ID) );
    $api_url = 'http://api.t.sina.com.cn/statuses/update.json';
    $body = array( 'status' => $status, 'source'=>'2615568240');
    $headers = array( 'Authorization' => 'Basic ' . base64_encode("$username:$password") );
    $result = $request->post( $api_url , array( 'body' => $body, 'headers' => $headers ) );
  }
}
</pre>

## RSS

此绑定试了一下又能用了（原理是RSS，有点不稳定，时间不能改）。[参考这里](http://weibo.com/tool/bloglink)。