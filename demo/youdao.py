#!/usr/bin/env python
# coding=utf-8
import os
import threading
import time

import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup
import base64
import json

class YouDao(object):
    name = ''
    password = ''
    cookie = None
    cookieFIle = './cookies.dat'
    isLogin = False

    def __init__(self):
        return

    def lookup(self,word):
        url = "http://dict.youdao.com/search?q=" + word + "&keyfrom=dict.index"
        content = urllib2.urlopen(url).read()
        doc = BeautifulSoup(content)
        transCont = doc.find('div',attrs={"class":"trans-container"})
        
        lis = transCont.findAll('li')
        for li in lis:
            print li.string

        additional = transCont.find('p',attrs={'class':'additional'})
        print additional.string
        return
def run(word):
    model = YouDao()
    model.lookup(word)

if __name__ == '__main__':
    word = raw_input("输入要查询的单词:  ")
    run(word)

