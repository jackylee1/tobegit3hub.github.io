+++
date = "2013-01-17T08:35:28+08:00"
draft = true
title = "note of python network"

+++



* /etc/services can show all the ports
* DNS is one of UDP application
* socket.socket(AF_INET, SOCK_STREAM), then connect()
* socket.makefile(), then readlines() or write()
* goherlib could just bulid the socket connection
* or urllib.urlopen(“”) and then just read()
* the type of interconnection includes IPv4, IPv6, IPX, AFP
* the family of protocol defines how the data transpots
* AF_INET is for IPv4, SOCK_STREM is for TCP and SOCK_DGRAM is for UDP
* socket.connect() needs a tuple of host and port
* we don’t need to use the actual ip address
* TCP and UDP use the same port, Oops, it depends on HTTP
* python is also controlled by OS
* SO_REUSEADDR is setted true for debugging
* empty parameters in bind() means all interfaces
* UDP server dosen’t need to listen()
* inetd uses port to distribute socket to its server
* only in Unix/Linux, find /etc/inetd.conf to configure
* all in /var/log
* in python, syslog.syslog() to record class and exception
* OS can provide DNS function with resolver library
* that’s /etc/hosts which Windows doesn’t get to define localhost
* PyDNS couldn’t access /etc/hosts, which is for DNS server
* half-open socket needs shutdown() to forbid
* use NULL(it’s ” in python) as sign character
* base64 is the format to print any binary digits
* different plantform gets each binary encoding, but a standard for net
* import struct and call htonl()
* socket.setsocketopt(SO_BROADCAST) to broadcast
* try not to broadcast except DHCP
* Oops, Steam Protocol is IPv5
* socket.getaddrinfo() to determinate INET or INET6
* select() is old, hervy and compatible with Windows
* urllib2.urlopen(rullib2.Request
* https is auto-supported, which depends on your version of Python
* urllib2.urlencode([(tuple)]), ranther than just adding the url
* HTMLParser.HTMLParser()
* for not well-formed html file, use htmlentitydefs
* you can access xml.dom, too
* RPC is for C while RMI is for Java, so just choose XML-RPC
* Python can use Zolera SOAP Infrastructure to use SOAP
* vMIME is short for Multipurpose Internet Mail Extension
* MIMEText and email to set ['to'], ['From'], ['Subject']
* email.Utils.formatdate() to set the header
* email.message_from_file() can load the email(just txt I mean)
* MIMEMutipart can access original MIMEText and other files
* import smtplib
* poplib.POP3(host, port), then user() and pass_() which is simple