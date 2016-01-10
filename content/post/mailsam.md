+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "mailsam"

+++



Python的优势在于网络编程，加上DRY的类库可以很便捷地实现一些网络功能，而且代码可读性很好，以下就实现了使用Gmail发邮件的功能（注意修改各自的username和password）。

<pre>
#! /usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.Message import Message
from time import sleep

smtpserver = 'smtp.gmail.com'
username = 'foo@gmail.com'
password = 'bar'
from_addr = 'tobeg3oogle@gmail.com'
to_addr = 'tobeg3oogle@gmail.com'
cc_addr = 'tobeg3oogle@gmail.com'

message = Message()
message['Subject'] = 'The title of this mail'
message['From'] = from_addr
message['To'] = to_addr
message['Cc'] = cc_addr
message.set_payload('The content of this mial')
msg = message.as_string()

sm = smtplib.SMTP(smtpserver, port=587, timeout=20)
sm.set_debuglevel(1)
sm.ehlo()
sm.starttls()
sm.ehlo()
sm.login(username, password)
sm.sendmail(from_addr, to_addr, msg)
sleep(5) #avoid calling quit() before sending the mail
sm.quit()
</pre>

