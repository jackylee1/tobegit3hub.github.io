+++
date = "2015-10-13T23:18:02+08:00"
draft = true
title = "Glance命令行使用文档"

+++

## 列举所有image

```
glance image-list
```

## 创建image

```
glance image-create --name test-image
```

## 删除image

```
glance image-delete ed1500da-d7fb-4dd5-a640-7837d7b32cc8
```

## 查看image详细信息

```
glance image-show ed1500da-d7fb-4dd5-a640-7837d7b32cc8
```

## 更新image信息

```
glance image-update ed1500da-d7fb-4dd5-a640-7837d7b32cc8 --name test-image2
```

## 下载image

```
glance image-download ed1500da-d7fb-4dd5-a640-7837d7b32cc8
```