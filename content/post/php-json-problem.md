+++
date = "2015-01-14T08:35:32+08:00"
draft = true
title = "php json problem"

+++



## Problem

The `json_encode` will escape the string for you.

## Solution

```
json_encode($str, JSON_UNESCAPED_SLASHES);
```

## Reference

* <http://php.net/manual/en/function.json-encode.php>
* <http://stackoverflow.com/questions/10210338/json-encode-escaping-forward-slashes>