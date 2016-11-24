
#-*- coding: UTF-8 -*- 

import urllib


def callback(a,b,c):
	'''
	@a: 
	@b:
	@c:
	'''
	down_progress = 100.0 * a * b / c
	if down_progress > 100:
		down_progress = 100
	print "%.2f%%" % down_progress




'''
1.闯入网址，网址的类型一定是字符串

2.传入的，本地的网页保存路径 + 文件名

3.一个函数的调用，可以任意来定义这个函数的行为,
但是一定要保证这个函数有3个参数.

(1)到目前为此传递的数据块数量。
(2)每个数据块的大小，单位的byte字节
(3)远程文件的大小(有时候返回 -1)
'''


url = "http://www.iplaypython.com/"

urllib.urlretrieve(url,"/home/adventurer/iplaypython.html",callback);
