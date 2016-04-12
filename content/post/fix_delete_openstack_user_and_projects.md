+++
date = "2016-04-13T00:09:21+08:00"
draft = true
title = "OpenStack误删User和Project后的故障恢复"

+++

## 简介

User和Project是OpenStack Keystone重要的数据，如果数据库没有定期备份，误删后数据库记录丢失，恢复起来比较麻烦。

目前最靠谱的方案是通过其他资源找到id，新建user和project，然后手动更新数据库保证id与以前一样，目前测试此方案可用。

## 实验数据

```
# original user id 
72abc4173d74449e8c9298ceae1b92b9
# original tenant id 
10bfa9fce03341ec98d788190224ee28

# new user id
4f5a21fcc63f46c3a6252d57cc45c8ef
# new project id
c38da856f1e14a0ba6ad34a7db75152e
```

## 恢复步骤

首先通过资源获取旧user id和旧project id。

```
cinder show e70ae3f6-48cf-4e6c-aac4-e78b339aeb27 
```

然后创建新的user和project，准备更新为被删的id。

```
openstack user create new_user
 
openstack project create new_project
```

接着进入keystone数据库，用旧的user id替换新的user id，因为有外键依赖因此需要删除和重建local_user数据。

```
mysql keystone
 
select * from user where id='4f5a21fcc63f46c3a6252d57cc45c8ef';
 
select * from local_user;
 
delete from local_user where user_id='4f5a21fcc63f46c3a6252d57cc45c8ef';
 
update user set id='72abc4173d74449e8c9298ceae1b92b9' where id='4f5a21fcc63f46c3a6252d57cc45c8ef';
 
select * from local_user;
 
insert into local_user (user_id, domain_id, name) values ( '72abc4173d74449e8c9298ceae1b92b9', 'default', 'new_user’);
```

然后用旧的project id替换成新的project id。

```
select * from project;
 
update project set id='10bfa9fce03341ec98d788190224ee28' where id='c38da856f1e14a0ba6ad34a7db75152e';
```

最后添加role。

```
role add --project new_project --user new_user admin
```

测试用新的user和project登录后可以看到旧user和旧project的所有资源！
