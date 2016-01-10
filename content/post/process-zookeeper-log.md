+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "process zookeeper log"

+++



Here's the code. I will format it later.

<pre>
require 'csv'

file = File.open("/home/tobe/temp/zk-log/ip1.log", "r")

hash = Hash.new

file.each_line do |line|
  ip = /\d+.\d+.\d+.\d+/.match(line)[0]

  if hash.has_key? ip
    hash[ip] = hash[ip] + 1
  else
    hash[ip] = 1
  end
end

CSV.open("/home/tobe/temp/zk-log/ip1.csv", "wb") {|csv|
  hash.to_a.each {|elem|
    csv << elem
  }
}
</pre>
