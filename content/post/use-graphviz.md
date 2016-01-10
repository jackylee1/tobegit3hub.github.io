+++
date = "2015-06-29T08:35:33+08:00"
draft = true
title = "use graphviz"

+++



## Installation

```
brew install graphviz
```

## Example

The simple.dot looks like this.

```
graph simple {
    a -- b;
    b -- c;
    b -- d;
    d -- a;
}
```

Run this command to generate the image.

```
dot -Tpng simple.dot -o simple.png
```

## Reference

* http://www.graphviz.org/Download_macos.php
* http://www.cnblogs.com/youxin/p/3527999.html
* http://casatwy.com/shi-yong-dotyu-yan-he-graphvizhui-tu-fan-yi.html