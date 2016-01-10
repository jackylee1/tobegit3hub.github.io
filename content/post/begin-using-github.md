+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "begin using github"

+++



1. 安装Git，注册GitHub

2. 生成ssh_key 

   ssh-keygen -t rsa -C “your_email@youremail.com”

3. 设置Git信息

    git config –global user.name “Your Name Here”  
    git config –global user.email “your_email@example.com”  
    git config –global credential.helper cache  

4. 创建repo
    
    git init  
    git add LICENSE.md  
    git commit -m ‘first commit’  
    git remote add origin https://github.com/username/Hello-World.git  
    git push origin master

5. 问题一

    error: server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none
    svn list https://github.com
    export GIT_SSL_NO_VERIFY=1

6. 问题二

    error: The requested URL returned error: 403
    modify .git/config file as url=ssh://git@github.com/derekerdmann/lunch_call.git
    git remote set-url origin https://yourusername@github.com/user/repo.git
    git remote -v

7. 问题三

    error: The requested URL returned error: 403 while accessing https://github.com/tobegit3hub/NotATop.git/info/refs
    改用ssh，git@github.com:tobegit3hub/NotATop.git

8. 问题四

    Permission denied (publickey).
    Check that you are connecting to the correct server

9. Finally

    cd ~/.ssh/ssh-keyg………….

