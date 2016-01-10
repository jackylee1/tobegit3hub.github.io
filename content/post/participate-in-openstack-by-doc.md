+++
date = "2016-01-10T08:35:32+08:00"
draft = true
title = "participate in openstack by doc"

+++



![](./openstack_logo.jpg)

## OpenStack社区概况

OpenStack的官方项目已经有154个项目，总代码行数累计超过四千万行，庞大的社区需要良好的文档来维护。OpenStack社区的文档可以说是任何开源项目都无法媲美的，每个组件都有详细的文档介绍，分别定义了格式良好的RESTful接口，甚至每个接口的参数都有详尽的解析。那我们如何通过文档来参与OpenStack社区呢？

官方文档地址 http://docs.openstack.org/

![](./openstack_doc.png)

## OpenStack文档规范

OpenStack是一组Python项目的集合，而Python最常用的文档工具是Sphinx，OpenStack也不例外。通过规范的RST文件格式，开发者可以轻易地编辑和修改，并生成格式良好的文档网站。

以OpenStack镜像服务Glance为例，所有文档都源文件都托管在GitHub上，就像这样。

![](./glance_doc_github.png)

在OpenStack官方网站的服务器上，获得Glance项目的源码后，通过一行命令`sphinx-build -b html source html`就可以将所有RST文件转化成标准格式的HTML文件，然后托管到Web服务器上。开发者在 http://docs.openstack.org/developer/glance/ 就可以看到最新的文档内容了。

![](./glance_doc.png)

OpenStack所有文档都是通过reStructuredText格式编写的，文件后缀为rst。这种轻量级标记语言与Markdown非常类似，通过添加易读的标签控制内容的样式，结合Sphinx工具可以将RST文本转化为LaTex、HTML或PDF等多种格式。目前GitHub已经支持在线渲染RST文件，如果你想为OpenStack共享文档，学习RST格式也是很有必要的，幸运的是RST非常容易上手。

通过阅读右面的中文教程很容易掌握RST语法 http://pm.readthedocs.org/zh_CN/latest/doc/sphinx.html ，通过阅读OpenStack的原始文档我们也很容易深入理解和学习。

## 通过文档贡献社区

阅读过Glance官方文档后，很荣幸我们发现了Bug，在“Controlling Glance Servers”小节出现了“configuation”这样的Typo，在GitHub上的原始文件也确认了这个问题。

![](./glance_doc_typo.png)

接下来我们得反馈给社区，贡献社区的第一步就是将这个Bug提出来让开发者可以确认。在OpenStack的官方文档中我们可以找到报Bug的launchpad网站地址，注册登录以后，我们就可以“Report a bug”填写必要的描述，最终这个Typo的Bug地址可以在这里找到 https://bugs.launchpad.net/glance/+bug/1455314

![](./typo_bug.png)

提出了Bug我们接着就可以尝试Fix它，OpenStack为第一次参与社区的开发者提供的非常详尽的文档 https://wiki.openstack.org/wiki/Documentation/HowTo/FirstTimers 。按照文档的说明，首先我们在OpenStack官网和launchpad注册了账号并添加自己的ssh key，然后在本地安装好git和git-review工具，这样就可以开始修改代码了。

由于只是文档错误，所以修改很简单，也不需要经过严谨的测试。本地把Glance项目clone下来后，checkout新的开发分支，修改拼写错误的文件，然后commit提交到本地。接着使用git review，这会自动将本地的修改提交到review服务器，社区其他开发者审查没问题后就可以提交到主干了，在开源社区的第一次贡献也就这样完成了。Review可能是个漫长的过程，无论是大小feature都需要通过这样的流程，具体的review界面如下。

![](./glance_patch.png)

## 翻译OpenStack中文文档

如果找不到官方文档的Bug也没关系，我们正在组织OpenStack官方文档的翻译，目前已经翻译了Glance项目的全部文档，你可以在这里看到 http://glancedoc.com/

![](./glance_doc_cn.png)

中文文档翻译会以官方文档为准，使用相同的格式与内容，Glance文档翻译如有纰漏可在这里修改贡献 https://github.com/tobegit3hub/glance-doc

通过文档参与OpenStack社区是很容易而且非常有意义的，欢迎大家参与！