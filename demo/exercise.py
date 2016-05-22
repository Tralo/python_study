#!/usr/bin/env python
# coding=utf-8
weight = 60
height = 1.65
result = weight / (height * height)
print('BMI的值为:  ',result)
if result < 18.5:
    print('过轻')
elif result < 25:
    print('正常')
elif result < 28:
    print('过重')
elif result < 32:
    print('肥胖')
else:
    print('严重肥胖')
