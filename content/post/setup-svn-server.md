+++
date = "2016-06-14T09:23:10+08:00"
draft = true
title = "set svn server"

+++

## Commands

```
svn import ~/code/a/aws/ file:///Users/tobe/temp/svn_temp/a/some/project/
svn list file:///Users/tobe/temp/svn_temp/a/some/project/
cd a/some/project
svn update
svn diff
svn checkout  file:///Users/tobe/temp/svn_temp/a/some/project/ ~/temp
svn list
```