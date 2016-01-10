+++
date = "2015-05-21T08:35:33+08:00"
draft = true
title = "docker copy file"

+++



## Volumn

Mount the local file system before running the container.

```
docker run -v /:/host
```

## Deocker exec

Use docker exec to make the file in the raw way.

```
cat localfile | docker exec -i  data sh -c 'cat > containerfile'
```

## Devicemapper

Just access the devicemapper directory.

```
cp thefile.txt /var/lib/docker/devicemapper/mnt/123abc<bunch-o-hex>/rootfs/root 
```

## Aufs

Just access the aufs directory.

```
ls /var/lib/docker/aufs/...
```