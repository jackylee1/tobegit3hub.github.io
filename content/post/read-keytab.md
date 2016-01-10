+++
date = "2014-08-22T08:35:32+08:00"
draft = true
title = "read keytab"

+++



With secure HBase cluster, we use kerberos for each use. Sometimes it's hard to locate the issue about kerberos. Here's a tool called `ktutil` which is short for "keytab util". Then run `rkt` that means "read keytab" to load the keytab file. Using `list` you can get the readable information from this binary file.

The following ouput is much easier to understand:

<pre>

➜  ~  ktutil
ktutil:  rkt /etc/h_chronos_admin.keytab
ktutil:  list
slot KVNO Principal
