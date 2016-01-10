+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "python socket programming"

+++



Socket编程可以实现Http服务器或者其他通讯的专用服务器，虽然很简单，还是贴一下代码。

SocketServer.py

<pre><code>

#! /usr/bin/python
# -*- coding: utf-8 -*-

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 4343))
serverSocket.listen(5)

while True:
  clientSocket, (clientHost, clientPost) = serverSocket.accept()
  print "Connection building..."
  clientSocket.send("Server said, hi")
  clientSocket.close()

</code></pre>

SocketClient.py

<pre><code>

#! /usr/bin/python
# -*- encoding: utf-8 -*-

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1", 4343))

print clientSocket.recv(16)

clientSocket.close()

</code></pre>