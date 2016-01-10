+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "note of head first python"

+++



* IDLE is like Shell, tab, alt+p, alt_n
* think of list in Python as a high level collection
* def print_lol(lists), if isinstance(item, list), print_lol(item)
* triple quote for multiple line comment
* from distutils.core import setup
* python setup.py dist means creating a tar and MANIFEST
* python setup.py install means copying my.py to /usr/total/lib/python2.7/dist_packets
* python create a namespace with the same name as your module
* Opoos, not allow to go to pypi.python.org
* BIF is short for Build-In Function
* true is not True
* os.getCwd() and os.chdir()
* (number, char) = string.split(“”)
* find() reture -1 if not found
* print(“XXX”, file=out)
* “finally:”, too
* locals() reture a collection of names defined in the current scope
* except IOError as err:
* the use of “with” negates the need for the “finally” suite
* sort() is in-place sorting and sorted() is copied sorting
* list comprehension, [ op for in ]
* remove duplicates with sets, set()
* create a class object without “new”
* every method’s first argument is “self”
* the “self” is important for unshared attribute
* list.__init__([])
* pop your code on PyPI, but not in China
* the dynamic content, Common Gateway Interface
* YATE is short for Yet Another Template Engine
* SL4A is short for Scripting Layer For Android
* install SL4A.apk and python_for_android.apk
* import android, app = android.Android(), app.makeToast()
* json works in both Python2 and Python3
* Python includes SQLite, import sqlite3
* .connect(), .cursor(), execute(), .commit(), .close()
* define database schema with XXX.sqlite
* GAE uses Python2.5
* Beautiful Soup for HTML parser
