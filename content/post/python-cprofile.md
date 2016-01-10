+++
date = "2016-01-10T08:35:33+08:00"
draft = true
title = "python cprofile"

+++



## Code

```
def add(first, second):
    return first + second

add(1,2)
```

## Command

```
python -m cProfile -o result ./use_cprofile.py
```

## Install

```
pip instal lpyprof2calltree
apt-get install kcachegrind
```

## Analyse

```
pyprof2calltree -k -i result.cprof
```


