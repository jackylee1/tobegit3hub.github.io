+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "three code implement quicksort"

+++



快排的思想是递归，如果用Python来实现只需要三行代码，第一行定义函数名，第二行定义初始条件，第三行实现递归。很神奇吧，来看看代码。

<pre><code>

def quicksort(array):
  if array==[]: return []
  else: return quicksort([x for x in array[1:] if x<array[0]]) + [array[0]] + quicksort([x for x in array[1:] if x>array[0]])

</code></pre>

因为Python是动态语言，所以在生成list（相当与数组）时可以不定义长度，根据与pivot比大小后动态生成，这也就是用C实现快排的麻烦之处。因此有人说Python更适合演示算法，在这里它就无需考虑数据的底层存储，根据条件动态生成长度不定的数组，这也是算法所不应该考虑的，于是可读性又好了。

有个问题，这样的话算法复杂度不好算，因为基本操作已不止是赋值或者交换了。不可能是list comprehension的复杂度吧，有机会一定要看看源码，有机会。