+++
date = "2016-04-04T08:19:49+08:00"
draft = true
title = "Python脚本使用Trace功能"

+++

## Trace介绍

Trace在计算机编程中有着广泛应用，在我们常用的编程脚本中，可以用于跟踪程序代码的执行。

在Shell脚本中，我们常加上`sex -x`命令，这样就可以答应程序执行的每一行，而Python也有对应的用法。

## Python的Trace功能

如果脚本比较简单，可以打印所有行，那么可以启动时加入trace参数。

```
python -m trace -t foo.py
```

如果想自定义trace格式，或者在特定代码打trace，可以自己实现一个函数，然后在代码中插入trace。

```
def mytrace(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        line = linecache.getline(sys.argv[0], lineno)
        if TRACING:
            print "%d: %s" % (lineno, line.rstrip())
    return mytrace

def test():
    TRACING.append(True)
    TRACING.pop()

sys.settrace(mytrace)
```

## 参考链接

* <http://stackoverflow.com/questions/15760381/what-is-the-python-equivalent-of-set-x-in-shell>
