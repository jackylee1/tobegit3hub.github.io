+++
date = "2016-04-12T23:57:50+08:00"
draft = true
title = "OpenStack平台之间迁移虚拟机和云硬盘"

+++

## 背景

客户需要从其他OpenStack迁移到我们的平台，或者在多个OpenStack集群之间迁移业务，这需要我们提供方案来迁移虚拟机和云硬盘。

目前只能做到基于Ceph的数据迁移保证数据不丢，迁移过程需要中断业务，而网络、云主机和云硬盘的对应关系等仍需要手动处理。

## 迁移虚拟机

注意，迁移失败可能导致业务数据丢失，因此建议先创建新的虚拟机演练迁移步骤。

首先是获取虚拟机id，通过虚拟机id去获取存储在Ceph中的rbd image id，一般是形如“xxxxxx_disk”这样的。

```
rbd -p openstack-00 ls |grep $nova_instance_id
```

然后把虚拟机根磁盘也就是这个rbd image导出到本地，注意本地需要预留足够的空间，一般Linux虚拟机占20G而Windows虚拟机占40G。

```
rbd -p openstack-00 export $rbd_image_id vm_file
```

导出本地后，可以拷贝到新的集群重新导入，为了让新虚拟机使用这个根磁盘需要先创建新的虚拟机，然后删除它的rbd image，导入数据生成新的rbd image。

```
# 创建虚拟机
nova boot --image xxx --flavor xxx --nic net=xxx new-vm
 
# 删除它的rbd image
rbd -p openstack-00 ls |grep $nova_instance_id
rbd -p openstack-00 rm $rbd_image
 
# 创建新rbd image并导入数据
rbd -p openstack-00 import vm_file --image $rbd_image
```

## 迁移云硬盘

迁移云硬盘与迁移云主机逻辑类似，需要导入rbd image，然后创建新的云硬盘后导入数据。

```
# 删除它的rbd image
rbd -p openstack-00 ls |grep $cinder_volume_id
rbd -p openstack-00 export $cinder_volume_id volume_file
 
# 创建新云硬盘
cinder create --name new_volume 100
 
# 删除它的rbd image
rbd -p openstack-00 ls |grep $cinder_volume_id
rbd -p openstack-00 rm $rbd_image

# 导入数据到新云硬盘
rbd -p openstack-00 import volume_file --image $cinder_volume_id
```
