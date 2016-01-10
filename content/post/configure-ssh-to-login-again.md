+++
date = "2015-07-03T08:35:33+08:00"
draft = true
title = "configure ssh to login again"

+++



## Configure SSH

```
mkdir ~/.ssh/socks
vim ~/.ssh/config
```

## Config

```
Host *
    KeepAlive yes
    ServerAliveInterval 60
    ControlMaster auto
    ControlPersist yes
    ControlPath ~/.ssh/socks/%h-%p-%r
```		    