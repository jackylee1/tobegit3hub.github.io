+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "note of django"

+++



* “python setup.py install” to install
* django has been moved from svn to github
* install mysql and get mysql-python and more
* just “django-admin.py startproject projectName”
* just “python manger.py runserver”
* if shared, make it 0.0.0.0:8080
* uncomment out to use set urls.py
* rewrite urls.py to match the views.py
* use a raw string in the url
* return HttpResponse(htmlString)
* the parameter captured should be string anytime
* raise Http404()
* getTemplate(), render(), context()
* render_to_response() in django.shortcuts
* locals() includes all the variables including request, as well
* template inheritance, inside-out and define the difference
* import MySQLdb, connect(), cursor(), execute(), fetchall()
* MTV for Model-Template-View is just like MVC
* class XXX(django.db.models.Model)
* first_name = models.charField(max_length=100)
* python manage.py sqlall books to generate “CREATE TABLE”
* 