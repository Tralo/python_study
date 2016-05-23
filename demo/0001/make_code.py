#!/usr/bin/env python
# coding=utf-8
from random import Random

def codeGenerator(number,codeLength = 15):
    print '*** Code Generator ***'
    codeFile = open('codes.txt','w')
    if number <= 0:
        return 'invalid number of codes'
    else:
        chars = 'abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        random = Random()
        for j in range(1, number + 1):
            str = ''
            for i in range(1, codeLength + 1):
                index = random.randint(1,len(chars))
                str = str + chars[index - 1]
            codeFile.write(str + '\n')

print codeGenerator(10)
