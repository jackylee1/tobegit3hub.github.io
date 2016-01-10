+++
date = "2016-01-10T08:35:30+08:00"
draft = true
title = "implement time in ruby"

+++



## Program 

Time is the linux tool to calculate the time the specified program consumed. 

## In Ruby

* read command name from ARGV
* Time.new and Time.now are the same
* to_i to change into integer
* system() to call local command
* sleep() to sleep

## Source Code

<pre><code>                                                      
#!/usr/bin/env ruby                                                                            

def calculate_time(command)
  return unless command
  puts "begin calculate time of #{command}"

  start_time = Time.now
  is_success = system(command)
  #sleep(50)                                                                                   
  end_time = Time.now
  consume_second = end_time - start_time
  consume_minute = (consume_second/60).to_i
  remaining_second = consume_second - consume_minute*60

  puts "#{command} is running #{is_success}"
  puts "calculate time is #{consume_minute} minutes and #{remaining_second} seconds"
end

if __FILE__ == $0
  command = ARGV.first
  calculate_time(command)
end
</code></pre>