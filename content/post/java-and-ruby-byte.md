+++
date = "2014-03-11T08:35:31+08:00"
draft = true
title = "java and ruby byte"

+++



## Basic

* Big-endian means little index with significant number, which is reasonable.

## Java Implement

<pre>
/**
 * Convert a long value to a byte array using big-endian.
 *
 * @param val value to convert
 * @return the byte array
 */
public static byte[] toBytes(long val) {
  byte [] b = new byte[8];
  for (int i = 7; i > 0; i--) {
    b[i] = (byte) val;
    val >>>= 8;
  }
  b[0] = (byte) val;
  return b;
}
</pre>

## Ruby Implement

<pre>
l = 0
bytes.each_byte do |byte|
  l = l << 8
  l ^= byte & 0xff
end  
</pre>

## Reference

* Big-endian and little-endian, <http://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Data/endian.html>
* Java Byte, <http://wenda.tianya.cn/question/590eb67c0ff77961>