+++
date = "2016-01-13T22:16:07+08:00"
draft = true
title = "swift tempurl middleware"

+++

## 介绍

tempurl是Swift提供的一项功能，允许其他用户在有限时间内临时下载某个object，同时不需要修改对象的访问权限。

## 使用tempurl

一个temp url是对应一个object的，包含temp_url_sig签名和temp_url_expires超时时间，格式如下。

```
https://swift-cluster.example.com/v1/AUTH_a422b2-91f3-2f46-74b7-d7c9e8958f5d30/container/object?temp_url_sig=da39a3ee5e6b4b0d3255bfef95601890afd80709&temp_url_expires=1323479485
```

要生成temp url，需要先生成这个用户的秘钥，也就是一个字符串，可以使用命令swift post -m "Temp-URL-Key:b3968d0207b54ece87cccc06515a89d4"，如果通过curl命令设置的HTTP header就是“X-Account-Meta-Temp-URL-Key”。

然后我们可以通过脚本生成一个HMAC签名，或者使用swift-temp-url脚本，注意我们是可以甚至temp url允许用户的行为例如POST、GET还是DELETE。

```
swift-temp-url GET 3600 /v1/AUTH_account/container/object mykey
```

通过curl就可以测试是否能匿名下载这个object。

```
curl -i "http://swift.example.com/v1/AUTH_bob/everyone_can_read_container/plan.txt?temp_url_sig=bc0e05d787ca0818ecbd8d61fa086e0e8514209a&temp_url_expires=1379716925"
```

还有更多高级用法，例如可以传参数或者header制定这个object的类型，让浏览器可以直接下载或使用。

## swift-temp-url实现原理

swift-temp-url就是生成url的脚本，这个脚本通过hmac生成签名，虽然可以生成任意url，但是否有效还是看Swift服务端的tempurl中间件的实现，实现也是非常简单的。

```
sig = hmac.new(key, '%s\n%s\n%s' % (method, expires, real_path), sha1).hexdigest()
print '%s?temp_url_sig=%s&temp_url_expires=%s' % (path, sig, expires)
```

## tempurl中间件实现原理

要使用tempurl功能，需要在paste使用tempurl，这时会在setup.cfg找tempurl，发现是这个类的函数swift.common.middleware.tempurl:filter_factory。

然后进入/swift/common/middleware/tempurl.py的filter_factory()函数，第一步是调register_swift_info()，根据是admin用户还是普通用户在执行swift info命令时输出是否支持tempurl这样的信息。

然后重点是创建TempURL类，在__init__()做简单的初始化工作。而用户请求来时，因为是wsgi应用所以会直接调用__call__()，第一步是调用_get_temp_url_info()来获取签名和expire时间。

如果method、sig和expire都没问题，就会使用同样的hmac库get_hmac()生成一样的签名，这个就需要先去后端获取用户的key，整个流程和用户生成tempurl是一样的。

下一步对生成的每一个hmac都判断一下有效性，如果无效就调用_invalid()返回401，如果有效就通过middleware继续调用，当然这里还支持了inline和disposition等高级特性。

## 参考链接

* 参考官方文档 http://docs.openstack.org/kilo/config-reference/content/object-storage-tempurl.html
* SwiftStack文档 https://swiftstack.com/docs/admin/middleware/tempurl.html
* swift-feature-highlight-tempurls https://swiftstack.com/blog/2015/01/29/swift-feature-highlight-tempurls/