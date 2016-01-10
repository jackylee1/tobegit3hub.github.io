+++
date = "2012-12-04T08:35:27+08:00"
draft = true
title = "note of design pattern"

+++



There are so many notes about Design Pattern on the Internet and here is mine. Having known the design patterns, reading the notes and checking out the client code are really useful before practice.

1. Simple Factory, give a parameter then return a instance.
2. Strategy, write a algorithm interface and context to call it.
3. Single Responsibility.
4. Open-close Principle.
5. Lisp Swap Principle, sub-class can replace super-class without attention.
6. Decorator, the decorator and the clother implements same interfaces and contains instance to call basic’s function firstly.
7. Proxy, proxy and the real object implements the same interface, then proxy gets an instance to control it.
8. Factory Method, new AddOperation() then call the inheritant function, then move the responsibility from server to client.
9. Prototype, calling clone() rather than construction.
10. Template Method, call the abstract function within the class to reduce code.
11. Law of Dimiter, two class communicate with the third member.
12. Facade, pass the request to lower operation, like Stoke.
13. Builder, constructor should call all the recommended methods.
14.Observer.
15. Abstract Factory, define the same operations of different factory or factory method.
16. State, abstract state and handleState().
17. Adapter.
18. Memento, class originator createMemeto() and caretaker set() and get() to store states.
19. Composite, the leaf and node extend the same super-class, then node contains list of children, add() and remove().
20. Iterator, implement first(), next() and isNull().
21. Singleton.
22. Bridge, a class can changes its impliementation as its attribute.
23. Command, make all requests as commands, then execute one by one.
24. Responsible Chain, a lower class can call upper class’s function to deal with stuff.
25. Mediator, there are abstract mediator and abstract and call the function.
26. Fly weight, something about light-weight.
27. Interpreter, different sub-class rewrite the function to explain the string.
28. Visitor, an abstract super-class has different op methods, then the concrete on just call one of them.

Because observer, adapter, iterator are used recently and factory, singleton are for Not-A-Top, the Android game. Therefore, they are written simply.