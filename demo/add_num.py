#!/usr/bin/env python
# coding=utf-8
from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('cool_quiet.ttf', size = 40)
    fillcolor = "#ff00ff"
    width, height = img.size
    draw.text((width-40, 0),'99',font = myfont, fill = fillcolor)
    img.save('result.jpg','jpeg')

if __name__ == '__main__':
    image = Image.open('touxiang.jpg')
    add_num(image)
