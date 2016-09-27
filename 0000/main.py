#!usr/bin/python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

picPath = 'pic.jpg'     #图片路径
textString = '3'        #要绘制的字符串
textSize = 50           #绘制大小
circR = 30          #绘制字符串的边界
colorFill = 'White'
colorFillCirc = 'Red'
imFont = ImageFont.truetype(r'c:\windows\fonts\msyh.ttf', textSize)

im = Image.open(picPath)

drawPosition = [im.size[0] - textSize +7, -5]
circPoint1 = (im.size[0] - 2 * circR, 0)
circPoint2 = (im.size[1], 2 * circR)
print(str(circPoint1) + str(circPoint2))

draw = ImageDraw.Draw(im)
draw.ellipse([circPoint1, circPoint2], fill = colorFillCirc)
draw.text(drawPosition, textString, colorFill, imFont)
im.save('picSave.jpg')
#im.show()
