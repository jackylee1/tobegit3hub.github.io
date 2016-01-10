+++
date = "2015-02-11T08:35:32+08:00"
draft = true
title = "test implement interface"

+++



## Unit Test

We should make sure some classes are implementing the interfaces.

## Code

```java
package foo;

import foo.Bar;
import junit.framework.Assert;
import org.junit.Test;

/**
 * Test {@link foo.Bar}
 */
 public class TestBar {

     @Test
     public void testImplementInterface() {
         Assert.assertTrue(Iface.class.isAssignableFrom(Bar.class));
     }
}
                      
```

## Reference

* <http://stackoverflow.com/questions/12145185/determine-if-a-class-implements-a-interface-in-java>