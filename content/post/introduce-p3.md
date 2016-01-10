+++
date = "2016-01-10T08:35:31+08:00"
draft = true
title = "introduce p3"

+++



## Introduction

The eariest and most simple way is the parameters after the command, like `ls -al /home/`.

For more complex programs, we normally use configuration file. It looks this:

<pre>
thread = 10
operations = 100000
rows = 100000
</pre>

They are all acceptable but not the best. Because I don’t know what options can I set for each key. Futhermore, the dependiencies between them are hidden and we hardly know what’s more can be setted. Then p3 file gives you the following advantage:

* browser all the options
* show the dependency
* easy to set if you use emacs
* friendly for multiple choices