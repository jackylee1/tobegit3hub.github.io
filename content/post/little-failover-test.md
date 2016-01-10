+++
date = "2016-01-10T08:35:31+08:00"
draft = true
title = "little failover test"

+++



## Fail

<pre>
#!/bin/bash                                                                                                                                                                                                         

echo "Start the script"

for (( ; ; ))
do

  delay=$(($RANDOM%600))
  echo "Sleep" $delay
  sleep $delay

  echo "Kill timestamp-server"
  ps aux |grep "timestamp-server" | grep -v "grep" | grep "java" | awk '{print $2}' |xargs kill

done

echo "End the script"
</pre>

## Recover

<pre>
God.watch do |w|

  w.name="ruby_loop"
  w.start="ruby /home/tobe/temp/ruby/ruby_loop.rb"
  w.keepalive

end
</pre>