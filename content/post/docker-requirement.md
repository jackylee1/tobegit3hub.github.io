+++
date = "2014-12-19T08:35:32+08:00"
draft = true
title = "docker requirement"

+++



## Introduction

Refer to <https://docs.docker.com/installation/centos/>, we have to upgrade Linux kernel to 2.6.32-431 or higher for docker. But why?

Because docker relies on LXC(Cgroups, Namespace and chroot) and aufs or devicemapper. And 2.6.32-431 kernel just supports part of theses features and all these projects're developing. I'm gonna list all the requirement of them.

## Cgroups

Cgroups was merged in Linux kernel in 2.6.24. But it can only control cpu or something. The control of memory which is also known as kmemcg was merge in 3.8. So don't satisify kernel 2.6.32 because it doesn't support kmemcg yet.

## Namespace

Linux namespace was merged in 2.6.23 and it updated from time to time. In kernel 3.12 it finally supported user namespace. Here're all the supported namespace.

```
UTS: hostname (this post)
IPC: inter-process communication (in a future post)
PID: “chroot” process tree (in a future post)
NS: mount points, first to land in Linux (in a future post)
NET: network access, including interfaces (in a future post)
USER: map virtual, local user-ids to real local ones (in a future post)
```

## Aufs

It seems not merged in Linux kernel. But it supports kernel 3.0+ well.

## Devicemapper

Device-mapper is a component of the 2.6 linux kernel.

