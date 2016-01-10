+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "j2ee error to start tomcat"

+++



在servers视图中启动tomcat,并访问tomcat默认首页http://localhost:8080/,如果8080端口被占用，可以将其设置为未被使用的端口号，重新访问。这时候会出现一个404错误，但是至少可以确定tomcat7配置正确。需要做的就是将安装目录的”webapp“下的ROOT文件夹复制到eclipse的工作空间的 “/.metadata/.plugins/org.eclipse.wst.server.core/tmp0/wtpwebapps“ 目录下进行覆盖。

启动服务器时出现异常：

<pre>
警告: Failed startup of context com.google.apphosting.utils.jetty.DevAppEngineWebAppContext@1242b11{/,E:\workspace\uploadPhoto\war}

Class: com.opensymphony.xwork2.spring.SpringObjectFactory
File: SpringObjectFactory.java
Method: getClassInstance
Line: 209 – com/opensymphony/xwork2/spring/SpringObjectFactory.java:209:-1
Caused by: java.lang.NullPointerException at com.opensymphony.xwork2.spring.SpringObjectFactory.getClassInstance(SpringObjectFactory.java:209)
</pre>

原因两个：

1. lib中多导入包的大原因：去掉struts2-spring-plugin-2.1.8包即可，因为没有用到spring。
2. 还有的原因是用spring了，却没加监听器，在web.xml里面加上使用org.springframework.web.context.ContextLoaderListener