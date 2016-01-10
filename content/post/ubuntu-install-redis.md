+++
date = "2015-03-18T08:35:32+08:00"
draft = true
title = "ubuntu install redis"

+++



## Introduction

It's super easy to install redis without finding and downloading any package.

## Install

```
apt-get update
apt-get upgrade
apt-get install redis-server
cp /etc/redis/redis.conf /etc/redis/redis.conf.default
```

## Run

```
redis-server /etc/redis/redis.conf
redis-cli
```

## Test

```
put 'foo', 'bar'
get 'foo'
```

