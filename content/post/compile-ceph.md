+++
date = "2016-01-10T08:35:33+08:00"
draft = true
title = "compile ceph"

+++



## Requirement

```
apt-get install -y autotools-dev
apt-get install -y automake
apt-get install -y pkg-config
apt-get install -y libsnappy-dev
apt-get install -y libleveldb1 libleveldb-dev
apt-get install -y libblkid-dev
apt-get install -y libudev-dev
apt-get install -y libkeyutils-dev
apt-get install -y libcrypto++-dev libcrypto++-doc libcrypto++-utils
apt-get install -y fuse
apt-get install -y libedit-dev
apt-get install -y libaio-dev
```

## 

```
git clone https://github.com/ceph/ceph
cd ceph/
./autogen.sh
./configure --without-fuse --without-tcmalloc --without-libatomic-ops --without-libxfs
make -j6
```


