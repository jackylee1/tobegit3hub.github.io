+++
date = "2014-01-02T08:35:31+08:00"
draft = true
title = "constructor call must be the fist statement in a constructor"

+++



## Synopsis

“Constructor call must be the fist statement in a constructor” is unreasonable

## Description

Mostly I call this() or super() in a constructor when I want to reuse the code to construct a object for variable parameters. And sometimes I don’t like to put the this() or super() in the first line because I wan’t to make all the parameters before calling them, but it’s contrary to the syntax of Java.

## Justification

I know it’s the rule to maintain the hierarchy of constructors and get rid of the risk to override the attributes we want to set. However, it deprives our right to initial the parameters before calling this() or super(). So I think we should be able to do this and be care about risk by ourselves.

## Expected Behavior

I hope we don’t have this restriction for programming in Java.

## Actual Behavior

Now we have the rule “Constructor call must be the fist statement in a constructor”.