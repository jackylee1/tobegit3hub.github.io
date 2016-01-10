+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "install different go"

+++



## Introduction

It's super easy to install different versions of golang.

## Install

```
bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
[[ -s "$HOME/.gvm/scripts/gvm" ]] && source "$HOME/.gvm/scripts/gvm"
gvm version
gvm install go1.4
gvm use go1.4
go version
```

