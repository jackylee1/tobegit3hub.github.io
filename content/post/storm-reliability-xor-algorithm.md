+++
date = "2015-06-15T08:35:33+08:00"
draft = true
title = "storm reliability xor algorithm"

+++



## Introduction of Storm

Storm is the distributed system to process stream data like what MapReduce does.

The task will be split into multiple parts which we call tuples and tuples have sub-tuples. Apprently, we have to finish this tuple tree before we think we get the task done.

Storm has the excellent reliability xor algorithm to make sure this is controllable.

## Xor Theory

```
1 xor 1 = 0
1 xor 0 = 1
0 xor 1 = 1
0 xor 0 = 0
```

So we know the xor two same elements will get the result 0. Then we get this.

```
A xor A xor B xor B xor C xor C ... = 0 
```

If anything appears exactly two times, we will always get 0.

## Storm Reliability Algorithm

![](storm_acker.jpg)

Storm has the acker to determine if the task is finished or not.

For each task, we allocate one message_id. And we have the ack_val which is 0 at the first time or when the task is finished.

Every time we create the tuple, we allocated a random 64 bits which calls tuple_id.

When we finish the current tuple, we send the tuple_id to `xor` the ack_val. If the result is 0, it seems everything done. But how?

Because if we have many tuples, we get this `tuple_id_0 xor (tuple_id_0 xor tuple_id_1) xor ...`. We will get 0 if all the tuples send exactily two messages to acker.

## More about Storm

The algorithm solve Out Of Memory problem when the tuple tree grows.

We also have the other id to callback the task owner.