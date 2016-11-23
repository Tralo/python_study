# -*- coding: utf-8 -*-


import urllib

url = "http://www.163.com/"

html = urllib.urlopen(url)

# print html.read().decode("gbk").encode("utf-8")

# print dir(html)

# print html.info()

# print html.getcode()

# print html.headers()

# print html.geturl()

# print html.next()
# print html.next()
# print html.next()

# print html.next()
# print html.next()


urllib.urlretrieve(url,"/home/adventurer/aaaa.txt")

