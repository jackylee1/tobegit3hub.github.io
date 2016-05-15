+++
date = "2016-05-15T11:20:30+08:00"
draft = true
title = "fix port scanning"

+++


SSH服务允许远程攻击者获得ssh的具体信息，如版本号等等。这可能为攻击者发动进一步攻击提供帮助。

解决办法是修改源代码或者配置文件改变SSH服务的缺省banner。

禁用Banner的方法是，vim /etc/ssh/sshd_config，添加一下这段。

```
Banner none
```

然后重启sshd服务。

```
systemctl restart sshd.service
```

为了提高httpd的安全性，避免服务器版本信息泄露，还可以通过修改/etc/httpd/conf/httpd.conf的配置项提高安全性。

```
ServerTokens ProductOnly
ServerSignature Off
TraceEnable Off
```

不过这些尽可能在我们环境先测试下，避免影响已有的服务。

```
根据绿盟提供的建议，可以和客户确认是否需要VNC功能，如果不需要我们可以关闭提高系统安全性。
```
