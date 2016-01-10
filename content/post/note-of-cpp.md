+++
date = "2016-01-10T08:35:29+08:00"
draft = true
title = "note of cpp"

+++



* C++是面向对象语言（数据抽象），即提供功能可以很方便地支持这种设计风格
* 记住写public、private，继承也要public继承
* 虽然CPP提供运算符重载，但是不用，可以提供函数来实现功能而且更直观
* 继承机制是从simula中学习过来的
* 通用型程序设计，用template来实现
* 来自main的非0值表示出错
* C风格字符串即以0字符结束的字符数组
* 读空格，getline(cin, str)
* 算法在std命名空间里，algorithm头文件
* wchar_t用于保存unicode字符，因为不是标准类型而是typedef
* 函数返回值不写void真的就是会削弱语法的规范性
* enum的sizeof是能够容纳该枚举的int的大小，绝对不会大于sizeof(int)
* 局部变量可以遮盖全局的，这与Java不同，：：x表示全局
* “abc”是constant char[4]，所以不能修改
* “==”比较的是指针，这肯定与Java不同
* 不存在指针到数组的隐式转换，只有数组到指针
* strlen()不会返回\0
* const char* 指向常量， char* const 常量指针，“*”之前都是const的一部份
* 引用不是一个对象，也不能像指针那样操作，可能被编译器优化掉
* argv的内型是char* [argc+1]
* \*p++ means \*(p++) not (\*P)++
* unknown sequence of “f(2)+g(3)”
* main is specially not return a value
* typedef int (*functionPointer) (int);可以定义函数指针来用
* 宏定义不能重载
* 利用宏可以设计自己的语言
