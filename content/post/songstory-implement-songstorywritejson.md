+++
date = "2013-04-22T08:35:29+08:00"
draft = true
title = "songstory implement songstorywritejson"

+++



<pre>
#!/usr/bin/env python
#coding=utf-8

import json


storyFile1 = open("1.txt", "r")
storyFile2 = open("2.txt", "r")
storyFile3 = open("3.txt", "r")
jsonFile = open("model.json", "r+")


jsonObject = json.load(jsonFile)
jsonObject["story_content_1"] = storyFile1.read().replace('"','\"')
jsonObject["story_content_2"] = storyFile2.read().replace('"','\"')
jsonObject["story_content_3"] = storyFile3.read().replace('"','\"')

newJson = json.dumps(jsonObject)

jsonFile.close()
storyFile1.close()
storyFile2.close()
storyFile3.close()


resultFile = open("model.json", "w+")

resultFile.write(newJson)
resultFile.close()
</pre>