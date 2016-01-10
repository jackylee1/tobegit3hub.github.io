+++
date = "2013-12-17T08:35:30+08:00"
draft = true
title = "solution for password"

+++



## Github

* <https://github.com/tobegit3hub/hehe.git>

## Introduction

1. First you need a universal [passphrase](http://en.wikipedia.org/wiki/Passphrase) to encrypt your password.

2. Then replace the real password with your generated password, and rename your file with suffix “.hehe”

3. For me, I get the config.json.hehe which looks like below.

    <pre>
    {
      "server":["106.187.93.241"],
      "server_port":15216,                                                                                                                                                                                        
      "local_port":1080,
      "password":"heheI0enj6E23Dwwjktlk4vxtA==hehe",
      "timeout":60,
      "method":"aes-256-cfb"
    }
    </pre>

4. Now it’s safe to upload on github because your password is encrypted by the algorithm [Blowfish](http://en.wikipedia.org/wiki/Blowfish_(cipher)), which is safe enough even though the program is open source).

5. So when you checkout the file from github, you can use the `hehe` tool to restore your password and automatically generate the original file without suffix “.hehe”.

6. Write a script and all can be done without manual control. Checkout your configurations from github, make the soft link and `hehe` to generate the uncrypted files.

## Reference

* <http://www.iteye.com/topic/800094>

