# -*- coding:utf-8 -*-
import urllib

url = "http://www.iplaypython.com/"
html = urllib.urlopen(url)

content = html.read()

code = html.getcode()

if code == 200:
	print "网页正常."
else:
	print "网页出现问题...."
