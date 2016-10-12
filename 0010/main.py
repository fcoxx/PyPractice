#!usr/bin/python

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import string
import random

imsize = (400, 100)#验证码图像的大小
saltcount = 10#噪声点的个数
strsizerange = (0.5, 0.9)#超过0.9的会超出图像
code = ['' ,'', '', '']#验证码
codesize = [0, 0, 0, 0]

im = Image.new('RGBA', imsize, 'white')
imdraw = ImageDraw.Draw(im)

#算是加点噪声
while saltcount > 0:
    imdraw.point(
                 (random.randint(0, imsize[0]), random.randint(0, imsize[1])),
                 'black'
                )
    saltcount = saltcount - 1

#产生字符的随机大小

#产生放置字母的位置



#产生验证码的内容

for letter in code:
    code[code.index(letter)] = random.choice(string.ascii_letters)

im.show()
