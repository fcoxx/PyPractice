#!usr/bin/python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

picPath = 'pic.jpg'     #图片路径
textString = '50'        #要绘制的字符串
textSize = 50           #绘制大小
borderDraw = 10          #绘制字符串的边界
colorFill = 'Red'
imFont = ImageFont.truetype(r'c:\windows\fonts\msyh.ttf', textSize)

im = Image.open(picPath)

drawPosition = [im.size[1] - textSize - borderDraw, borderDraw]

draw = ImageDraw.Draw(im)
draw.text(drawPosition, textString, colorFill, imFont)
im.save('picSave.jpg')
