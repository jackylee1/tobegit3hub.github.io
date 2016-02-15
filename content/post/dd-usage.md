+++
date = "2016-02-15T09:02:19+08:00"
draft = true
title = "dd usage"

+++

## Introduction

Dd is the Linux tool to copy files. For more infomation please refer to <https://en.wikipedia.org/wiki/Dd_(Unix)> .

## Usage

```
dd bs=1M count=100 if=/dev/zero of=/var/images/test
```

Or use `urandom` to benchmark the device.

## Monitor 

```
killall -USR1 dd
```

## dcfldd

Dd is kind of out-of-dated and we should use the enhanced tool, dcfldd.

The parameters of `dcfldd` is the same as `dd`.

```
dcfldd bs=1M count=100 if=/dev/zero of=/var/images/test
```