+++
date = "2014-09-02T08:35:32+08:00"
draft = true
title = "jinfo bug"

+++



## jinfo crashed the JVM occasionally

<http://stackoverflow.com/questions/25568908/jinfo-crashed-the-jvm-occasionally>

Accidentally I found the stat of one Java process is T(Stopped, either by a job control signal or because it is being traced). I think it may be related to jinfo because I ran this command at that time. Then I try to run jinfo again and the process crashed agagin. But it's not easy to reproduce.

Does anyone have the idea of why the stat of process became T without kill -SIGSTOP? Does jinfo have bug which may crash the process?

EDIT: I have 100% reproduced this issue when jinfo the process which has ran over 60 days. The bug seems to be triggered if the process has ran for a long time. It doesn't work for the new processes.

OMG, jmap has the same issue and it's also 100% reproduced. But not for jstack. Now I'm so sure it's something about detecting jvm.

Here're the known issue about `jinfo`, <https://bugs.openjdk.java.net/browse/JDK-7167069?page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel> and <https://access.redhat.com/solutions/721793>.

## Disastrous bug when running jinfo and jmap

<http://stackoverflow.com/questions/25617763/disastrous-bug-when-running-jinfo-and-jmap>

When I run jinfo or jmap to any Java process, it will "suspend" the Java process. It's 100% reproduced for the long running processes.

Here're the detailed steps:

1. Pick a Java process which is running over 25 days(It's wired because this doesn't work for new processes).
2. Run ps to check the state of the process, should be "Sl" which is expected.
3. Run jinfo or jmap to this process(BTY, jstack doesn't have this issue).
4. Run ps to check the state of the process. This time it changes to "Tl" which means STOPPED and the process doesn't response any requests.

Here's the output of our process:

<pre>
[work@hadoop ~]$ ps aux |grep "qktst" |grep "RegionServer"
work     36663  0.1  1.7 24157828 1150820 ?    Sl   Aug06  72:54 /opt/soft/jdk/bin/java -cp /home/work/app/hbase/qktst-qk/regionserver/:/home/work/app/hbase/qktst-qk/regionserver/package//:/home/work/app/hbase/qktst-qk/regionserver/package//lib/*:/home/work/app/hbase/qktst-qk/regionserver/package//* -Djava.library.path=:/home/work/app/hbase/qktst-qk/regionserver/package/lib/native/:/home/work/app/hbase/qktst-qk/regionserver/package/lib/native/Linux-amd64-64 -Xbootclasspath/p:/home/work/app/hbase/qktst-qk/regionserver/package/lib/hadoop-security-2.0.0-mdh1.1.0.jar -Xmx10240m -Xms10240m -Xmn1024m -XX:MaxDirectMemorySize=1024m -XX:MaxPermSize=512m -Xloggc:/home/work/app/hbase/qktst-qk/regionserver/stdout/regionserver_gc_20140806-211157.log -Xss256k -XX:PermSize=64m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/home/work/app/hbase/qktst-qk/regionserver/log -XX:+PrintGCApplicationStoppedTime -XX:+UseConcMarkSweepGC -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:SurvivorRatio=6 -XX:+UseCMSCompactAtFullCollection -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+CMSParallelRemarkEnabled -XX:+UseNUMA -XX:+CMSClassUnloadingEnabled -XX:CMSMaxAbortablePrecleanTime=10000 -XX:TargetSurvivorRatio=80 -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=100 -XX:GCLogFileSize=128m -XX:CMSWaitDuration=2000 -XX:+CMSScavengeBeforeRemark -XX:+PrintPromotionFailure -XX:ConcGCThreads=16 -XX:ParallelGCThreads=16 -XX:PretenureSizeThreshold=2097088 -XX:+CMSConcurrentMTEnabled -XX:+ExplicitGCInvokesConcurrent -XX:+SafepointTimeout -XX:MonitorBound=16384 -XX:-UseBiasedLocking -XX:MaxTenuringThreshold=3 -Dproc_regionserver -Djava.security.auth.login.config=/home/work/app/hbase/qktst-qk/regionserver/jaas.conf -Djava.net.preferIPv4Stack=true -Dhbase.log.dir=/home/work/app/hbase/qktst-qk/regionserver/log -Dhbase.pid=36663 -Dhbase.cluster=qktst-qk -Dhbase.log.level=debug -Dhbase.policy.file=hbase-policy.xml -Dhbase.home.dir=/home/work/app/hbase/qktst-qk/regionserver/package -Djava.security.krb5.conf=/home/work/app/hbase/qktst-qk/regionserver/krb5.conf -Dhbase.id.str=work org.apache.hadoop.hbase.regionserver.HRegionServer start
[work@hadoop ~]$ jinfo 36663 > tobe.jinfo
Attaching to process ID 36663, please wait...
Debugger attached successfully.
Server compiler detected.
JVM version is 20.12-b01
[work@hadoop ~]$ ps aux |grep "qktst" |grep "RegionServer"
work     36663  0.1  1.7 24157828 1151008 ?    Tl   Aug06  72:54 /opt/soft/jdk/bin/java -cp /home/work/app/hbase/qktst-qk/regionserver/:/home/work/app/hbase/qktst-qk/regionserver/package//:/home/work/app/hbase/qktst-qk/regionserver/package//lib/*:/home/work/app/hbase/qktst-qk/regionserver/package//* -Djava.library.path=:/home/work/app/hbase/qktst-qk/regionserver/package/lib/native/:/home/work/app/hbase/qktst-qk/regionserver/package/lib/native/Linux-amd64-64 -Xbootclasspath/p:/home/work/app/hbase/qktst-qk/regionserver/package/lib/hadoop-security-2.0.0-mdh1.1.0.jar -Xmx10240m -Xms10240m -Xmn1024m -XX:MaxDirectMemorySize=1024m -XX:MaxPermSize=512m -Xloggc:/home/work/app/hbase/qktst-qk/regionserver/stdout/regionserver_gc_20140806-211157.log -Xss256k -XX:PermSize=64m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/home/work/app/hbase/qktst-qk/regionserver/log -XX:+PrintGCApplicationStoppedTime -XX:+UseConcMarkSweepGC -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:SurvivorRatio=6 -XX:+UseCMSCompactAtFullCollection -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+CMSParallelRemarkEnabled -XX:+UseNUMA -XX:+CMSClassUnloadingEnabled -XX:CMSMaxAbortablePrecleanTime=10000 -XX:TargetSurvivorRatio=80 -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=100 -XX:GCLogFileSize=128m -XX:CMSWaitDuration=2000 -XX:+CMSScavengeBeforeRemark -XX:+PrintPromotionFailure -XX:ConcGCThreads=16 -XX:ParallelGCThreads=16 -XX:PretenureSizeThreshold=2097088 -XX:+CMSConcurrentMTEnabled -XX:+ExplicitGCInvokesConcurrent -XX:+SafepointTimeout -XX:MonitorBound=16384 -XX:-UseBiasedLocking -XX:MaxTenuringThreshold=3 -Dproc_regionserver -Djava.security.auth.login.config=/home/work/app/hbase/qktst-qk/regionserver/jaas.conf -Djava.net.preferIPv4Stack=true -Dhbase.log.dir=/home/work/app/hbase/qktst-qk/regionserver/log -Dhbase.pid=36663 -Dhbase.cluster=qktst-qk -Dhbase.log.level=debug -Dhbase.policy.file=hbase-policy.xml -Dhbase.home.dir=/home/work/app/hbase/qktst-qk/regionserver/package -Djava.security.krb5.conf=/home/work/app/hbase/qktst-qk/regionserver/krb5.conf -Dhbase.id.str=work org.apache.hadoop.hbase.regionserver.HRegionServer start
</pre>

It may be the bug of JVM but I don't get any response after I reported this to oracle. So I hope some JVM experts here could help.

> $ java -version   
> java version "1.6.0_37"  
> Java(TM) SE Runtime Environment (build 1.6.0_37-b06)  
> Java HotSpot(TM) 64-Bit Server VM (build 20.12-b01, mixed mode)
