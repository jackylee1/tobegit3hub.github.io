+++
date = "2015-06-25T08:35:33+08:00"
draft = true
title = "pip setup uninstall"

+++



## Uninstall with setup.cfg

```
python setup.py install --record files.txt
cat files.txt | xargs rm -rf
```