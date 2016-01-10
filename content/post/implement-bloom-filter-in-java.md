+++
date = "2016-01-10T08:35:29+08:00"
draft = true
title = "implement bloom filter in java"

+++



<pre>
package cn.chendihao.mybloomfilter;

import java.util.BitSet;

public class MyBloomFilter {

    private static final int DEFAULT_SIZE = 1 << 25; // 2**25
    
    private static final int[] seeds = new int[] { 5, 7, 11, 13, 31, 37, 61 }; // k hash
    
    private BitSet bits = new BitSet(DEFAULT_SIZE);
   
    private MyHash[] hashObjects = new MyHash[seeds.length];

    
    public static void main(String[] args) {
       String value = "www.chendihao.cn";
       
       MyBloomFilter filter = new MyBloomFilter();
       
       System.out.println(filter.contains(value));
       
       filter.add(value);
       
       System.out.println(filter.contains(value));
    }
    
    
    public MyBloomFilter() {
       for (int i = 0; i < seeds.length; i++) {
           hashObjects[i] = new MyHash(DEFAULT_SIZE, seeds[i]);
       }
    }


    public void add(String value) {
       for (MyHash f : hashObjects) {
           bits.set(f.hash(value), true);
       }
    }


    public boolean contains(String value) {

       if (value == null) {
           return false;
       }

       for (MyHash f : hashObjects) {
           boolean isSet = bits.get(f.hash(value));
           if(isSet == false){
               return false;
           }
//           result = result && bits.get(f.hash(value));
       }
       return true;
    }

    
    public static class MyHash {
       
       private int capacity;
       private int seed;

       public MyHash(int capacity, int seed) {
           this.capacity = capacity;
           this.seed = seed;
       }

       public int hash(String value) {
           int result = 0;
           int len = value.length();
           for (int i = 0; i < len; i++) {
              result = seed * result + value.charAt(i);
           }
           return (capacity - 1) & result;
       }
    }
    
}
</pre>