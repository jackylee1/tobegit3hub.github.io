+++
date = "2016-01-10T08:35:31+08:00"
draft = true
title = "chronos release process"

+++



1. git checkout -b chronos-1.1-release
2. git push -u origin chronos-1.1-release
3. edit pom
4. git commit
5. git push origin chronos-1.1-release
6. git tag -a chronos-1.1.0-release -m “release chronos-1.1.0″
7. git push origin chronos-1.1.0-release
8. git checkout master
9. git branch -D chronos-1.1-release
10. git checkout chronos-1.1.0-release
11. mvn deploy -DskipTests