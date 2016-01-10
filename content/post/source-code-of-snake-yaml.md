+++
date = "2016-01-10T08:35:31+08:00"
draft = true
title = "source code of snake yaml"

+++


          
## Implement

* Node is the basic object in the graph.
* Tag means the type of Node.
* NodeTuple is the key-value pair which are both Node.
* Four types of Node, Scalar, Sequence, Map and Anchor.
* Any object could implement Represent to become Node.
* Representer will convert value into Node.
* Use Ragel for state machine as lexer
* Constructor to convert Node into object.
* Dumper needs to know the Representer and DumpOption.
* System.getProperty(“line.separator”) to generate different code.
* Emitter and Serialize help to write the Node.
* Yaml just dump or load from to stream.
* Object->Node->Serialization->Presentation

## Source Code

* hg clone https://code.google.com/p/snakeyaml/
* https://code.google.com/p/snakeyaml/source/checkout

## Reference

* <http://yaml.org/spec/1.1/>
* <http://www.complang.org/ragel/>
* <http://thingsaaronmade.com/blog/a-simple-intro-to-writing-a-lexer-with-ragel.html>