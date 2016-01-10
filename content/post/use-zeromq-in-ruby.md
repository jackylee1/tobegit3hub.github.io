+++
date = "2013-12-24T08:35:30+08:00"
draft = true
title = "use zeromq in ruby"

+++



## Push Server

<pre><code>
#!/usr/bin/env ruby                                                                            

require "ffi-rzmq"

def main

  context = ZMQ::Context.create(1)

  push_socket = context.socket(ZMQ::PUSH)
  push_socket.setsockopt(ZMQ::LINGER, 0)
  push_socket.bind("tcp://127.0.0.1:4343")

  push_socket.send_string("you look good")
  puts "I have send a string"

end

if __FILE__ == $0
  main
end
</code></pre>

## Pull Client

<pre><code>
#!/usr/bin/env ruby                                                                             

require "ffi-rzmq"

def main

  context = ZMQ::Context.create(1)

  pull_socket = context.socket(ZMQ::PULL)
  pull_socket.setsockopt(ZMQ::LINGER, 0)
  pull_socket.connect("tcp://127.0.0.1:4343")

  result = ""
  pull_socket.recv_string(result)
  puts "I have receive a string, #{result}"

end

if __FILE__ == $0
  main
end
</code></pre>

## Reference

* <https://github.com/andrewvc/learn-ruby-zeromq>
* <http://zguide.zeromq.org/py:all>