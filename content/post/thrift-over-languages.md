+++
date = "2013-11-18T08:35:30+08:00"
draft = true
title = "thrift over languages"

+++



## Thrift File

* namespace is not necessary
* i64 is for long
* then thrift --gen java or others

<pre>
namespace java com.xiaomi.infra.timestamp

service TimestampService{
  i64 get_timestamp()
}
</pre>

## Implement Interface

* add thrift to pom.xml
* copy the java file

<pre>
public class TimestampImplement implements TimestampService.Iface{
  
  private int timestamp = 0;

  public synchronized long get_timestamp() throws TException {

    return timestamp++;
  }

}
</pre>

## Java Server

* should new Args object
* TBinaryProtocol for efficience
* TThreadPoolServer for multi-thread blocked model

<pre>
    try {
      TServerSocket serverTransport = new TServerSocket(7911);
      Factory proFactory = new TBinaryProtocol.Factory();
      TProcessor processor = new TimestampService.Processor(new TimestampImplement());
      Args rpcArgs = new Args(serverTransport);
      rpcArgs.processor(processor);
      rpcArgs.protocolFactory(proFactory);
      
      TServer server = new TThreadPoolServer(rpcArgs);
      System.out.println("Start server on port 7911...");
      server.serve();
    } catch (TTransportException e) {
      e.printStackTrace();
    }
</pre>

## Java Client 

* mvn exec:java -Dexec.mainClass="com.xiaomi.infra.timestamp.TimestampClient" to execute

<pre>
    try {
      TTransport transport = new TSocket("localhost", 7911);
      transport.open();
      TProtocol protocol = new TBinaryProtocol(transport);
      TimestampService.Client client = new TimestampService.Client(protocol);
      
      long timestamp = client.get_timestamp();
      System.out.println("get the timestamp "+timestamp);
      transport.close();
    } catch (TTransportException e) {
      e.printStackTrace();
    } catch (TException e) {
      e.printStackTrace();
    }
</pre>

## Python

* sudo pip install thrift

<pre>
#!/usr/bin/env python                                                                          

import sys
sys.path.append('./gen-py/')

from timestamp import TimestampService
from timestamp.ttypes import *
from timestamp.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
  # Make socket                                                                                
  transport = TSocket.TSocket('localhost', 7911)

  # Buffering is critical. Raw sockets are very slow                                           
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol                                                                         
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder                                                
  client = TimestampService.Client(protocol)

  # Connect!                                                                                   
  transport.open()

  timestamp = client.get_timestamp()
  print timestamp


  transport.close()

except Thrift.TException, tx:
  print "%s" % (tx.message)
</pre>

## Ruby Client

<pre>
#!/usr/bin/env ruby                                                                            

$:.push('./gen-rb')

require 'thrift'
require 'timestamp_service'

begin
  transport = Thrift::BufferedTransport.new(Thrift::Socket.new('localhost', 7911))
  protocol = Thrift::BinaryProtocol.new(transport)
  client = TimestampService::Client.new(protocol)

  transport.open()

  result = client.get_timestamp

  puts result.inspect

  transport.close()
rescue
  puts $!
end
</pre>
