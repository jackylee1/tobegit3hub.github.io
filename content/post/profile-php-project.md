+++
date = "2014-11-20T08:35:32+08:00"
draft = true
title = "profile php project"

+++



There's a configuration file to setup the PHP cgi stuffs.

Try run `ps aux |grep "php-fpm" |grep -v "grep" |wc -l` to find out current worker processes.

No need to run too many processes because each one may use ~20M memory.

Just configurate `pm.max_children` in that configuration file.

Another important parameter is `pm.max_requests` which controlls when to restart work processes. This should be much larger than the default value otherwise processes restart quickly and raise the CPU usage.

We should set `showlog` and `request_slowlog_timeout` as well. We can know if the max_children is enough by anaylising the log.

