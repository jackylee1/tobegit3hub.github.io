+++
date = "2014-04-24T08:35:31+08:00"
draft = true
title = "django update schema"

+++



1. python ./manage.py syncdb

2. python manage.py convert_to_south monitor

3. check migration

4. edit model

5. python ./manage.py schemamigration monitor –auto

6. check migration

7. python manage.py migrate monitor