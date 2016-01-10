+++
date = "2014-10-15T08:35:32+08:00"
draft = true
title = "use google calendar api zh"

+++



## 源代码
* https://github.com/tobegit3hub/google_calendar_api_demo

## API文档
* <https://developers.google.com/google-apps/calendar/get_started>
* <https://developers.google.com/google-apps/calendar/v3/reference/events/insert>

## 开发步骤
1. 申请Google账号
2. 创建应用并授权使用Google Calendar API
3. 配置Java和Maven开发环境
4. 下载官方Demo和用户配置文件
5. 查看文档熟悉API的使用

## 代码实现
* 修改配置文件

<https://github.com/tobegit3hub/google_calendar_api_demo/blob/master/src/main/resources/client_secrets.json>

* 添加插入Event代码，需要修改邮箱地址

<https://github.com/tobegit3hub/google_calendar_api_demo/blob/master/src/main/java/com/google/api/services/samples/calendar/cmdline/CalendarSample.java>
