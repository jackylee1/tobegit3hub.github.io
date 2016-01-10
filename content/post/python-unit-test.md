+++
date = "2016-01-10T08:35:31+08:00"
draft = true
title = "python unit test"

+++



## Source Code
<pre>
class MyMath:
                                                                                                                                                                                                                    
  @staticmethod
  def add(n, m):
    return n + m
</pre>

## Test Code
<pre>
from my_math import MyMath
import unittest

class TestMyMath(unittest.TestCase):
  def test_add(self):
    result = MyMath.add(1, 2)
    self.assertTrue(result == 3)

if __name__ == "__main__":                                                                                                                                                                                          
  unittest.main()
</pre>

## Reference
* <http://blog.csdn.net/nie312122330/article/details/7994389>
