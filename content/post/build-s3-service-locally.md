+++
date = "2015-08-09T08:35:33+08:00"
draft = true
title = "build s3 service locally"

+++



## Video

<http://v.youku.com/v_show/id_XMTMwNTI1NDg0NA>

## Commands

* docker run -d --net=host -e MON_IP=96.126.127.93 -e CEPH_NETWORK=96.126.127.0/24 ceph/demo
* docker exec -i -t 2da099e23752 /bin/bash
* ps aux
* ceph -s
* radosgw-admin user create --uid=johndoe --display-name="John Doe" --email=john@example.com
* apt-get update -y
* apt-get install -y python
* apt-get install -y python-pip
* pip install boto
* pip install ipython
* ipython
* pip install s3cmd
* apt-get install -y vim
* vim ~/.s3cfg
* s3cmd ls

## Links

* <https://github.com/ceph/ceph>
* <https://github.com/ceph/ceph-docker>
* <http://ceph.com/docs/v0.80.5/radosgw/s3/python/>
* <https://github.com/boto/boto>
* <https://github.com/s3tools/s3cmd>
