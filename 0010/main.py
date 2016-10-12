#!usr/bin/python

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import string
import random
import time

imsize = (800, 200)#验证码图像的大小
saltcount = 10000#噪声点的个数
strsizerange = (0.5, 0.9)#超过0.9的会超出图像
code = ['' ,'', '', '']#验证码
codesize = [0, 0, 0, 0]
codepos = [(0,0), (0,0), (0,0), (0,0)]
codefont = [0, 0, 0, 0]

im = Image.new('RGBA', imsize, 'white')
imdraw = ImageDraw.Draw(im)

#产生字符的随机大小
codesizeindex = 0
while codesizeindex < 4:
    codesize[codesizeindex] = int(imsize[1] * random.uniform(strsizerange[0], strsizerange[1]))
    codesizeindex = codesizeindex + 1

#产生放置字母的位置
#横坐标
posx0 = random.randint(0, imsize[0] - codesize[0] - codesize[1] - codesize[2] - codesize[3])
posx1 = random.randint(posx0 + codesize[0], imsize[0] - codesize[1] - codesize[2] - codesize[3])
posx2 = random.randint(posx1 + codesize[1], imsize[0] - codesize[2] - codesize[3])
posx3 = random.randint(posx2 + codesize[2], imsize[0] - codesize[3])

#纵坐标
posy0 = random.randint(0, imsize[1] - codesize[0])
posy1 = random.randint(0, imsize[1] - codesize[1])
posy2 = random.randint(0, imsize[1] - codesize[2])
posy3 = random.randint(0, imsize[1] - codesize[3])

codepos = [(posx0, posy0), (posx1, posy1), (posx2, posy2), (posx3, posy3)]
#产生验证码的内容

for letter in code:
    code[code.index(letter)] = random.choice(string.ascii_letters)

#设置字体
codefont[0] = ImageFont.truetype(r'c:\windows\fonts\consola.ttf', codesize[0])
codefont[1] = ImageFont.truetype(r'c:\windows\fonts\consola.ttf', codesize[1])
codefont[2] = ImageFont.truetype(r'c:\windows\fonts\consola.ttf', codesize[2])
codefont[3] = ImageFont.truetype(r'c:\windows\fonts\consola.ttf', codesize[3])

imdraw.text(codepos[0], code[0], 'black', codefont[0])
imdraw.text(codepos[1], code[1], 'black', codefont[1])
imdraw.text(codepos[2], code[2], 'black', codefont[2])
imdraw.text(codepos[3], code[3], 'black', codefont[3])

#算是加点噪声
while saltcount > 0:
    imdraw.point((random.randint(0, imsize[0]), random.randint(0, imsize[1])), 'blue' )
    saltcount = saltcount - 1

im.filter(ImageFilter.DETAIL)

time = time.strftime("%Y%m%d%H%M%S", time.localtime())

imname = 'code_' + time + '.jpg'

im.save(imname)
