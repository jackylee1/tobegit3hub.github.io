+++
date = "2014-10-04T08:35:32+08:00"
draft = true
title = "implement your ruby dsl zh"

+++



作为开发者，我们都希望设计一门最适合自己的语言，借助Ruby这个愿望很容易就可以实现。Ruby的语法比较宽松（调用函数时参数写不写括号都可以），非常适合做内部DSL（领域相关语言），难怪Ruby的生态如Rails、Gem、Rake、RSpec、Cucumber都有各自的DSL，当然内部DSL也是必须遵循Ruby的语法而不像SQL这种外部DSL那么灵活，使用自己设计的DSL可以节省我们后续的开发和维护工作，现在主流的运维工具如Puppet、Chef和God也都是用Ruby实现的。

[Oh_my_tpp](https://github.com/tobegit3hub/oh_my_tpp)是我自己实现一套语法，用于描述一个PPT的内容，目前已经实现将我定义的.omt文件转化为能够由tpp程序识别的.tpp文件。我们可以简单对照一下，下面是一个普通的.tpp文件。

    --title oh my tpp
    text The dsl for ppt, inspired by tpp.
    link https://github.com/tobegit3hub/oh_my_tpp.git

    --newpage
    --title syntax
    text the simple text like oh_my_tpp
    link the linke like https://travis-ci.org
    image the image in https://images.google.com
    audio the audio in https://fb.com
    video the video in https://www.youtube.com

而我实现的.omt可以将内容封转得更有语义化，如下。

    page "oh my tpp" do
      text "The dsl for ppt, inspired by tpp."
      link "https://github.com/tobegit3hub/oh_my_tpp.git"
    end

    page "syntax" do
      text "the simple text like oh_my_tpp"
      link "the linke like https://travis-ci.org"
      image "the image in https://images.google.com"
      audio "the audio in https://fb.com"
      video "the video in https://www.youtube.com"
    end

虽然我们设计了自己的语法，但我们还是要写程序来解释这段“代码”，实际上这段“代码”是符合Ruby语法规则的，利用Ruby强大的`instance_eval()`函数我们就可以执行这个文件，然后自定义`page()`、`text()`、`link()`、`image()`、`audio()`和`video()`这些函数，将对应的内容以固定格式写到一个tpp文件中，即实现了我们对这段“代码”的解析。当然我们也可以解析成一个HTML页面或者是一个真实的PPT文件，这完全取决于你程序的逻辑，而这种自定义的omt文件格式，更有利于非本专业的人员来编写。

此项目的源代码托管在[Github]()，主要的解释文件是[omt.rb](https://github.com/tobegit3hub/oh_my_tpp/blob/master/lib/omt.rb)，它主要是读取.omt文件，然后调用相应的函数来处理。而实际转化为.tpp文件的逻辑在[omt_tpp.rb](https://github.com/tobegit3hub/oh_my_tpp/blob/master/lib/omt_tpp.rb)中，为每一页创建"--newpage"的字符，相应的内容也写到.tpp文件中，可以看一下代码实现。

    # basic class to load .omt file
    class OhMyTpp
      attr_accessor :pages, :file_name

      def initialize
        @pages = []
      end

      def load(file_name)
        puts "[omt] load the file #{file_name}"
        @file_name = file_name
        self.instance_eval(File.read(file_name))
      end

      def page(title, &block)
        puts "[omt] load the page #{title}"
        page = Page.new(title)
        page.instance_eval(&block)
        @pages << page
      end

      def to_s
        @pages
      end

    end

omt_tpp.rb

    def make_tpp_file(tpp_file_name, pages)
      File.open(tpp_file_name, "w") do |file|

        pages.each_with_index do |page, index|
          puts "[omt tpp] write page #{page.title} into tpp"
          file.puts "--newpage" unless index==0

          file.puts "--title #{page.title}"
          page.contents.each do |kv|
            puts "[omt tpp] write #{kv.values[0]}"
            file.puts kv.keys[0].to_s << " " << kv.values[0]
          end
          file.puts ""
        end

      end
    end

