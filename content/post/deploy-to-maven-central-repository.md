+++
date = "2014-08-05T08:35:31+08:00"
draft = true
title = "deploy to maven central repository"

+++



1. Signup in sonatype website.
2. Edit your settings.xml in .m2 and pom.xml of your project.
3. `mvn deploy` should work.
4. Or Just upload your package with jar and pom.xml.

## Reference

* <http://central.sonatype.org/>
* <http://central.stage.sonatype.org/pages/apache-maven.html>
* <https://oss.sonatype.org/#view-repositories>