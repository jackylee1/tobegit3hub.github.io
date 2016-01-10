+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "maven thrift plugin zh"

+++



[Maven](http://maven.apache.org/)是一个项目管理和自动化构建工具，绝大部分Java项目如SSH框架、JUnit和Hadoop都使用Maven来管理，个人项目如果依赖这些框架只需在pom.xml申明所依赖的项目与版本即可。Maven自身提供了一套易拓展的程序框架，任何开发者都可以通过编写插件的形式拓展Maven的功能，以满足自身的需求。

[Thrift](http://thrift.apache.org/)是由Facebook开发用于实现跨语言RPC通信的开源框架，开发者通过定义.thrift接口文件，即可自动生成各种语言的服务端和客户端代码，而且提供了多种高效的通信模型，极大地减少了我们开发RPC程序的重复工作。使用Thrift前需要定义好.thrift文件，使用thrift程序生成对应语言的代码，然后加入到项目的源码中即可。

[Maven-thrift-plugin](https://github.com/dtrott/maven-thrift-plugin)是一个开源的Maven的插件，由于生成Thrift代码需要额外的命令，为了使构建更加自动化，使用这个插件只需在pom.xml申明这个插件并配置好参数，在Maven编译项目过程中就会自动为.thrift文件生成对应的Java代码并加入到你的项目中，这个过程就无须开发者参与了。

这是一个比较通用的需求，而maven-thrift-plugin是实现这个需求最好的实现了，我们也可以通过这个小程序（只有4个源文件差不多800行代码）了解如何开发一个Maven的插件以达到自己的要求，源代码可以在这里获得，<https://github.com/dtrott/maven-thrift-plugin>。

1. 要编写Maven插件，可以先参考这个[官方文档](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)，介绍了一个Hello World插件开发的完整步骤。
2. 依此我们看看maven-thrift-plugin这个项目，首先是[pom.xml](https://github.com/dtrott/maven-thrift-plugin/blob/master/pom.xml)这个自解释的文件，我们可以看到这个项目的描述，必须依赖的`maven-plugin-api`，还有用于测试的`JUnit`和方便执行命令行的`plexus-utils`。
3. 然后根据Maven的项目组织结构找到org.apache.thrift.maven包里面的[Thrift.java](https://github.com/dtrott/maven-thrift-plugin/blob/master/src/main/java/org/apache/thrift/maven/Thrift.java)，这是项目封装的工具类，在构造函数里面传入参数，然后拼接成最终要执行的命令，可以看到这里调用thrift命令指定生成的语言就是Java。
4. 然后看到[AbstractThriftMojo.java](https://github.com/dtrott/maven-thrift-plugin/blob/master/src/main/java/org/apache/thrift/maven/AbstractThriftMojo.java)，这是集成AbstractMojo.java实现插件关键逻辑功能的一个类，定义的虚函数是为了方便实际编译和测试编译的时候重写，核心功能在`execute()`这个函数中。首先是检测参数并构建出一个Thrift工具类的对象，然后在命令行执行构建好的命令，最后处理一下错误和日志。
5. 最后我们看一下[ThriftCompileMojo.java](https://github.com/dtrott/maven-thrift-plugin/blob/master/src/main/java/org/apache/thrift/maven/ThriftCompileMojo.java)和[ThriftTestCompileMojo.java](https://github.com/dtrott/maven-thrift-plugin/blob/master/src/main/java/org/apache/thrift/maven/ThriftTestCompileMojo.java)，这是我们实际执行的Java类，重写基类的虚函数是为了区分实际编译和测试编译的文件路径，核心功能还是前面提到的ThriftCompileMojo.java。这里顺便提一下Maven里面的mojo是Maven plain Old Java Object的意思，插件类也都是一个普通的java类而已.
6. 使用这个插件也很简单，在你项目的pom.xml加入[README](https://github.com/dtrott/maven-thrift-plugin/blob/master/README)提到的`plugin`标签，执行`mvn compile`就可以将你所有的 .thrift文件生成相应的Java文件，并且放置到你指定的目录上。

