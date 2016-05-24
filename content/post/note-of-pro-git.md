+++
date = "2016-05-24T09:12:01+08:00"
draft = true
title = "note of pro git"

+++

Git remove but keep the file.

```
git rm --cached foo
```

Git log to display the detailed code.

```
git log -p -2
```

Display all commit message.

```
git log --pretty=oneline
```

List some tags.

```
git tag -l "1.1.*"
```

Make the annotated tag.

```
git tag -a v1.4 -m 'my version 1.4'
```

Git tag for older commits.

```
git tag -a v1.2 9fceb02
```

Setup Gitweb server.

```
git instaweb --httpd=webrick
```

Merge patch file.

```
git apply --check foo.patch
```

Get more info about the branch.

```
git describe foo_branch
```

Get more info about the commit.

```
git show foo_commit
```

Stash files.

```
git stash 
git stash list
git stash apply stash@{0}
git stash show stash@{0} -p
```