#!/usr/bin/python
#Filename : write.py
import sys
import time
title = sys.argv[1]
time =  time.strftime('%Y-%m-%d',time.localtime(time.time()))
filename = time + '-' + title + '.html'
newfile = file(filename,'w')
head = '---\n' + 'layout: post\n' + 'title: ' + title + '\n---\n'
newfile.write(head)
