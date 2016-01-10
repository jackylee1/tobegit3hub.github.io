+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "github start a new project"

+++



1. create repo in github.com
2. git init
3. git remote add origin https://github.com/username/Hello-World.git
4. git add .
5. git commit -m “something done”
6. export GIT_SSL_NO_VERIFY=1(It might be a bug of Ubuntu!!)
7. git pull origin
8. git push -u origin master