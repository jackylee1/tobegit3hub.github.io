+++
date = "2016-04-02T10:40:12+08:00"
draft = true
title = "python_basic_and_tips"

+++

## 像其他语言那些for循环

```
for i, x in enumerate(array):
  do_something(i, x)
```

## 启动HTTP服务器

```
python -m SimpleHTTPServer
```

如果是Python 3可以更简化。

```
python -m http.server
```

## 使用Json工具

```
python -m json.tool
```

## 快速正确打开中文文件

```
with io.open("/Users/tobe/test.txt", "r", encoding="utf-8") as file:
    print(file.readlines())
```