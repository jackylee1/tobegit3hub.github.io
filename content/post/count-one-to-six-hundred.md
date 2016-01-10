+++
date = "2014-03-16T08:35:31+08:00"
draft = true
title = "count one to six hundred"

+++



## Manuscript

![](/images/one_to_six_hundred_1.jpg)

![](/images/one_to_six_hundred_2.jpg)

![](/images/one_to_six_hundred_3.jpg)

![](/images/one_to_six_hundred_4.jpg)

![](/images/one_to_six_hundred_5.jpg)

## Code

> 1692 

<pre>
count = 0
600.times do |i|
  count += i.to_s.length
end

puts count # 1690
</pre>