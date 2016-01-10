+++
date = "2015-03-17T08:35:32+08:00"
draft = true
title = "ubuntu upgrade docker"

+++



## Introduction

Docker 1.5 has much more functions than older versions. If you want to upgrade docker in ubuntu, please follow these processes.

## Remove the older

```
sudo apt-get autoremove docker.io
sudo apt-get purge docker.io
sudo apt-get autoremove lxc-docker
sudo apt-get purge lxc-docker
```

## Add the source

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
sudo sh -c "echo deb https://get.docker.com/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
sudo apt-get update
```

## Install latest docker

```
sudo apt-get install lxc-docker
```

