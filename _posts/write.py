#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Filename : write.py
import sys
import time
import os

if len(sys.argv) < 2:
	print "您忘了输入标题！"
	sys.exit()
tag = []
tagstr = ''
category = []
categorystr = ''
tagflag = False
categoryflag = False
for arg in sys.argv:
	if arg == "-t":
		tagflag = True
		categoryflag = False
	elif arg == "-c":
		categoryflag = True
		tagflag = False
	else:
		if tagflag :
			tag.append(arg)
		elif categoryflag :
			category.append(arg)		
print tag
print category
if tag:
	tagstr = "tags:\n"
	for atag in tag:
		tagstr = tagstr + '- ' + atag + '\n'
if category:
	categorystr =  "categories:\n"
	for acategory in category :
		categorystr = categorystr + '- ' + acategory +'\n'	
title = sys.argv[1]
time =  time.strftime('%Y-%m-%d',time.localtime(time.time()))
filename = time + '-' + title + '.md'
newfile = file(filename,'w')
head = '---\n' + 'layout: post\n' + 'title: ' + title +'\n' + tagstr + categorystr +'---\n'
newfile.write(head)
newfile.close()
os.system('vim  ' + filename)
