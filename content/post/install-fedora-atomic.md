+++
date = "2015-05-28T08:35:33+08:00"
draft = true
title = "install fedora atomic"

+++



Refer to official document in http://www.projectatomic.io/docs/quickstart/

1. Download qcow2 image in https://getfedora.org/cloud/download/
2. Convert into vdi by `qemu-img convert -f qcow2 [filename].qcow2 -O vdi [filename].vdi`
3. Install virtualbox
4. Create the virtual machine from that vdi file
5. Write the meta-data and user-data files
6. Generate iso file by `genisoimage -output init.iso -volid cidata -joliet -rock user-data meta-data`
7. Start virtual machine with this iso file

```
$ cat meta-data
instance-id: id-local01
local-hostname: samplehost.example.org
```

```
$ cat user-data
#cloud-config
password: mypassword
ssh_pwauth: True
chpasswd: { expire: False }

ssh_authorized_keys:
  - ssh-rsa ... foo@bar.baz (insert ~/.ssh/id_rsa.pub here)
```
