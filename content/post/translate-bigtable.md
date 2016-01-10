+++
date = "2013-11-01T08:35:30+08:00"
draft = true
title = "translate bigtable"

+++



# Bigtable是一个分布式结构化数据存储系统

## 概括来说

Bigtable是一个分布式存储系统为了管理结构化数据很大很大的，保存在上千台普通服务器的一千T级别数据。很多项目在Google都保存在Bigtable上，网页索引啦，Google地球啦，和Google金融。这些应用对Bigtable有不同的要求，不但在数据的大小上，还在对延迟的需求上。除了这些不同的要求，Bigtable还很好的提供了灵活的、高性能的解决方案给Google的特写产品。在这篇论文里面我们就描述了Bigtable提供的简单的数据模型，但可以给客户端提供动态的数据层格式的控制，然后我们描述Bigtable的设计与实现。

## 简介一下

在过去的两年半里我们已经设计和实现并部署了一个分布式存储系统去管理Google的机构化数据，名字就叫做Bigtable。Bigtable是设计用于可靠地拓展PB级数据到上千台服务器上。Bigtalbe已经已经实现这些目标：广泛的应用性，可拓展性，高性能和高可用性。Bigtable正用于超过60个Google的产品与项目，包括Google分析，Google金融，Orkut…