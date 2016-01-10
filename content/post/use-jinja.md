+++
date = "2015-07-08T08:35:33+08:00"
draft = true
title = "use jinja"

+++



## Introduction

Jinja2 is the template library which is used by OpenStack trove project.

## Install

```
pip install jinja2
```

## Usgae

```
>>> from jinja2 import Template
>>> template = Template('Hello {{ name }}!')
>>> template.render(name='John Doe')
u'Hello John Doe!'
```		    