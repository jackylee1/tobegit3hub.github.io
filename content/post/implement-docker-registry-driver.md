+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "implement docker registry driver"

+++



## Docker-registry

[Docker-registry](https://github.com/docker/docker-registry) is the index server to store docker images. Docker Hub is the official and largest registry from Docker Inc and everyone can build the private registry with the open-source project, docker-registry.

## Driver

Docker-registry supports multiple backend storage, such as file and AWS S3. If you want to store docker images in other storage, you need to implement the driver for specified backend storage.

Fortunately docker-registry provides a pluggable mechanism and you just need to rewrite the API to access your backend storage. There're some third-party drivers from developers around the world.

* [docker-registry-driver-gcs](https://github.com/dmp42/docker-registry-driver-gcs)
* [docker-registry-driver-qiniu](https://github.com/zhangpeihao/docker-registry-driver-qiniu)
* [docker-registry-driver-hdfs](https://github.com/lyda/docker-registry-driver-hdfs)
* [docker-registry-driver-sinastorage](https://github.com/kerwin/docker-registry-driver-sinastorage)
* [docker-registry-driver-swift](https://github.com/bacongobbler/docker-registry-driver-swift)

## Implement

Now I'm implementing the docker-registry driver for FDS. FDS is short for "File Data Storage" and it's the S3-like service from [Xiaomi Inc](http://mi.com). They have provided Python SDK named galaxy-fds-sdk to get and put objects.

All we have to is cloning the project [docker-registry-core](https://github.com/docker/docker-registry/tree/master/depends/docker-registry-core) and rewrite the APIs in the new file. The [file.py](https://github.com/docker/docker-registry/blob/master/depends/docker-registry-core/docker_registry/drivers/file.py) shows that we have to implement the `driver.Base` class, `get_content()`, `put_content()`, `stream_read()`, `stream_write()`, `list_directory()`, `exists`, `remove()` and `get_size()`. 

### file.py

```

class Storage(driver.Base):

    supports_bytes_range = True

    def __init__(self, path=None, config=None):
        self._root_path = path or './tmp'

    def _init_path(self, path=None, create=False):
        path = os.path.join(self._root_path, path) if path else self._root_path
        if create is True:
            dirname = os.path.dirname(path)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        return path

    @lru.get
    def get_content(self, path):
        path = self._init_path(path)
        try:
            with open(path, mode='rb') as f:
                d = f.read()
        except Exception:
            raise exceptions.FileNotFoundError('%s is not there' % path)

        return d

    @lru.set
    def put_content(self, path, content):
        path = self._init_path(path, create=True)
        with open(path, mode='wb') as f:
            f.write(content)
        return path

    def stream_read(self, path, bytes_range=None):
        path = self._init_path(path)
        nb_bytes = 0
        total_size = 0
        try:
            with open(path, mode='rb') as f:
                if bytes_range:
                    f.seek(bytes_range[0])
                    total_size = bytes_range[1] - bytes_range[0] + 1
                while True:
                    buf = None
                    if bytes_range:
                        # Bytes Range is enabled
                        buf_size = self.buffer_size
                        if nb_bytes + buf_size > total_size:
                            # We make sure we don't read out of the range
                            buf_size = total_size - nb_bytes
                        if buf_size > 0:
                            buf = f.read(buf_size)
                            nb_bytes += len(buf)
                        else:
                            # We're at the end of the range
                            buf = ''
                    else:
                        buf = f.read(self.buffer_size)
                    if not buf:
                        break
                    yield buf
        except IOError:
            raise exceptions.FileNotFoundError('%s is not there' % path)

    def stream_write(self, path, fp):
        # Size is mandatory
        path = self._init_path(path, create=True)
        with open(path, mode='wb') as f:
            try:
                while True:
                    buf = fp.read(self.buffer_size)
                    if not buf:
                        break
                    f.write(buf)
            except IOError:
                pass

    def list_directory(self, path=None):
        prefix = ''
        if path:
            prefix = '%s/' % path
        path = self._init_path(path)
        exists = False
        try:
            for d in os.listdir(path):
                exists = True
                yield prefix + d
        except Exception:
            pass
        if not exists:
            raise exceptions.FileNotFoundError('%s is not there' % path)

    def exists(self, path):
        path = self._init_path(path)
        return os.path.exists(path)

    @lru.remove
    def remove(self, path):
        path = self._init_path(path)
        if os.path.isdir(path):
            shutil.rmtree(path)
            return
        try:
            os.remove(path)
        except OSError:
            raise exceptions.FileNotFoundError('%s is not there' % path)

    def get_size(self, path):
        path = self._init_path(path)
        try:
            return os.path.getsize(path)
        except OSError:
            raise exceptions.FileNotFoundError('%s is not there' % path)

```

### fds.py

It's not hard to understand the meaning of these methods. Because the SDK of FDS is much like S3, I can put and get the objects like this.

```

    @lru.get                                                                                                                                                                                                        
    def get_content(self, path):                                                                                                                                                                                    
        try:                                                                                                                                                                                                        
            path = self._init_path(path)                                                                                                                                                                            
            return self.client.getObject(self.bucket, path)                                                                                                                                                         
        except:                                                                                                                                                                                                     
            raise exceptions.FileNotFoundError("File not found %s" % path)  

    @lru.set                                                                                                                                                                                                        
    def put_content(self, path, content):
        try:                                                                                                                                                                                                        
            path = self._init_path(path)                                                                                                                                                                            
            self.client.putObject(self.bucket, path, content)                                                                                                                                                       
        except:                                                                                                                                                                                                     
          raise IOError("Could not put content: %s" % path)                                                                                                                                                         
        return path

```

Make sure that you have thrown `FileNotFoundError` when the file doesn't exist. I was stuck in [#682](https://github.com/docker/docker-registry/issues/682) and thanks @dmp42 for the help.

The `stream_read()` and `stream_write()` may be the hardest part for me.  Then I ask the FDS guys to provide the similar APIs and the final code looks like that.

```

    def stream_read(self, path, bytes_range=None):                                                                                                                                                                  
        #self.buffer_size = 128 * 1024                                                                                                                                                                              
        path = self._init_path(path)                                                                                                                                                                                
        try:                                                                                                                                                                                                        
            for i in self.client.streamGetObject(self.bucket, path, self.buffer_size):
                yield i                                                                                                                                                                                             
        except:                                                                                                                                                                                                     
            raise exceptions.FileNotFoundError("File not found %s" % path)
                                                                                                                              
    def yield_content(self, fp):                                                                                                                                                                                    
        #self.buffer_size = 128 * 1024                                                                                                                                                                              
        while True:
            buf = fp.read(self.buffer_size)
            if not buf:
                break
            yield buf

    # Stream put object in FDS                                                                                                                                                                                      
    def stream_write(self, path, fp):
        path = self._init_path(path)
        self.client.streamPutObject(self.bucket, path, self.yield_content(fp))

```

I'm surprised with `yield` and have no idea how to implement the driver without it. In the method `stream_read()` we just get the piece of data and `yield` to the caller. In order to rewrite `stream_write()`, the FDS SDK provides  `streamPutObject()` to accept a generator function as parameter. And we have to accept `fp` and `yield` the content in `yield_content()` before requesting FDS service.

There's one more thing to notice. The `list_directory()` should return all the files and directories as well. The rest of the methods are not difficult to implement if the APIs are given.

## Conclusion

Thanks to the pluggable mechanism, implementing your docker-registry driver is not so hard. But there're also something you have to notice. The easiest way to do that is mimicing the `file.py` and "trial-and-error".

The docker-registry v2 is coming out. Notice that this driver may not work for v2 but anyway thanks for the great job of docker-registry team.