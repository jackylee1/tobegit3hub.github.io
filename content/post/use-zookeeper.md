+++
date = "2016-01-10T08:35:30+08:00"
draft = true
title = "use zookeeper"

+++




## Configuation

<pre><code>
# The number of milliseconds of each tick                                                                                                                                                      
tickTime=2000
# The number of ticks that the initial                                                                                                                                                         
# synchronization phase can take                                                                                                                                                               
initLimit=10
# The number of ticks that can pass between                                                                                                                                                    
# sending a request and getting an acknowledgement                                                                                                                                             
syncLimit=5
# the directory where the snapshot is stored.                                                                                                                                                  
# do not use /tmp for storage, /tmp here is just                                                                                                                                               
# example sakes.                                                                                                                                                                               
dataDir=/tmp/zookeeper
# the port at which the clients will connect                                                                                                                                                   
clientPort=2181
#                                                                                                                                                                                              
# Be sure to read the maintenance section of the                                                                                                                                               
# administrator guide before turning on autopurge.                                                                                                                                             
#                                                                                                                                                                                              
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance                                                                                                                   
#                                                                                                                                                                                              
# The number of snapshots to retain in dataDir                                                                                                                                                 
#autopurge.snapRetainCount=3                                                                                                                                                                   
# Purge task interval in hours                                                                                                                                                                 
# Set to "0" to disable auto purge feature                                                                                                                                                     
#autopurge.purgeInterval=1
</code></pre>

## Example

<pre><code>
package cn.chendihao.example.zookeeper;

import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.WatchedEvent;
import org.apache.zookeeper.ZooKeeper;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.ZooDefs.Ids;

public class ZookeeperExample {

  private static ZooKeeper zk;

  private static Watcher watcher = new Watcher() {
    public void process(WatchedEvent event) {
      System.out.println("processing");
    }
  };

  public static void main(String[] argv) throws Exception {
    zk = new ZooKeeper("localhost:2181", 30000, watcher);

    zk.create("/test", "it's a test".getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.PERSISTENT);
    System.out.println(new String(zk.getData("/test", watcher, null)));

    zk.setData("/test", "it's a new test".getBytes(), -1);
    System.out.println(new String(zk.getData("/test", watcher, null)));

    zk.delete("/test", -1);

    zk.close();
  }

}
</code></pre>

## pom.xml

groupId: org.apache.zookeeper

artifactId: zookeeper

version: 3.4.4-mdh1.0.0-SNAPSHOT
