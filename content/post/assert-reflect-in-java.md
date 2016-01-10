+++
date = "2014-03-19T08:35:31+08:00"
draft = true
title = "assert reflect in java"

+++



## Wrong

<pre>
ActionProvider actionProvider = ActionProviderFactory.createActionProvider(HBaseActionProvider.class.getName());
Assert.assertTrue(HBaseActionProvider.class.isInstance(actionProvider));
</pre>

## Solution

<pre>
ActionProvider actionProvider = ActionProviderFactory.createActionProvider(HBaseActionProvider.class.getName());
Assert.assertTrue(actionProvider.getClass().equals(HBaseActionProvider.class));
</pre>