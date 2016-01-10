+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "pycss 1.0 with source codemd"

+++



<pre>
#! /usr/bin/env python
# -*- encoding: utf-8 -*-

''' convert .pcss into .css '''

import sys

def main():

  pcssFileName = sys.argv[1]
  if not pcssFileName.endswith('.pcss'):
  print("Not a pcss file, exiting...")
  return False
  pcssFile = open(pcssFileName, 'r')

  cssFileName = pcssFileName[:-5] + '.css'
  cssFile = open(cssFileName, 'w')

  try:
    isInBlock = False

    for line in pcssFile:

      # empty line
      if not line.split():
        newLine = '\n'
        if isInBlock:
          newLine = '}' + '\n' + '\n'
          isInBlock = False

      # comment line
      elif line.startswith('#'):
        newLine = '/* ' + line[1:-1] +' */' + '\n'

      # selector line
      elif line.split() and not line.startswith('\t'):
        newLine = line.strip() + '{' + '\n'
        isInBlock = True

      # attribute line
      elif line.startswith('\t'):
        newLine = '\t' + line.strip() + ';' + '\n'
        cssFile.write(newLine)

    if isInBlock:
      newLine = '}' + '\n'
      cssFile.write(newLine)

    except IOError as e:
      print(e)
      finally:
      pcssFile.close()
      cssFile.close()

if __name__ == '__main__':
  main()
</pre>

What has been done:

* Detect whether input parameter is pcss file or not.
* Convert into css file with the same file name in the same directory.
* Translate Python comment into Css comment.
* Replace all braces with representative tab.
* Remove all semicolon at the end of each line.
* Ddd close brace in a new line even if EOF is the last line of attribute.
* Keep all the empty lines.
* Produce css file with readable tab as well.
