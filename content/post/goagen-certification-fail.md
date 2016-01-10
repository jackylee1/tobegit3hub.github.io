+++
date = "2013-02-26T08:35:28+08:00"
draft = true
title = "goagen certification fail"

+++



certutil -d sql:$HOME/.pki/nssdb -A -t TC -n “goagent” -i CA.crt

Ubuntu 系统：

1. 打开 Chrome 浏览器
2. 首选项 > 高级选项 > 管理证书…
3. 在 授权中心 导入 GoAgent/local 目录下的 CA.crt 证书（注意不要导入到 服务器 ，否则不起作用）
4. 在 授权中心 找到 GoAgent CA 并点击 修改…
5. 修改信任设置为全部选中
6. 重启浏览器
7. finally check certification “Check for server certificate revocation”