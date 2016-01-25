+++
date = "2015-12-19T23:20:09+08:00"
draft = true
title = "Cinder命令行使用文档"

+++

## 创建卷

```
cinder create 1

cinder create 1 --volume-type ssd

cinder create 1 --volume-type sata
```

## 列举所有卷

```
cinder list
```

## 删除卷

```
cinder delete $volume_id
```

## 强制删除卷

```
cinder force-delete $volume_id
```

## 重命名卷

```
cinder rename $volume_id $volume_name
```

## 查看卷详情

```
cinder show $volume_id
```

## 重置卷状态

```
cinder reset-state $volume_id
```

## 设置metadata

```
cinder metadata $volume set $key=$value
```

## 查看metadata

```
cinder metadata-show $volume_id
```

## 取消metadata

```
cinder metadata $volume unset $key
```

## 创建snapshot

```
cinder snapshot-create $volume_id
```

## 列举所有snapshot

```
cinder snapshot-list
```

## 删除snapshot

```
cinder snapshot-delete $snapshot_id
```

## 设置snapshot metadata

```
cinder snapshot-metadata $snapshot_id set $key=$value
```

## 查看snapshot metadata

```
cinder snapshot-metadata-show $snapshot_id
```

## 取消snapshot metadata

```
cinder snapshot-metadata $snapshot_id unset $key
```

## 显示卷类型

```
cinder type-list
```

## 创建卷类型

```
cinder type-create $type_name
```

## 删除卷类型

```
cinder type-delete $type_id
```

## 列举后端服务

```
cinder service-list
```
