#!/usr/bin/python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

im1 = Image.open('pic.jpg')
im2 = Image.open('pic2.jpg')
#im3 = Image.blend(im1, im2, 0.5)
#im3 = Image.composite(im1, im2, 0.5)
#im3.show()
#print(im1.getpixel((10, 10)))
#im1.putpixel((10, 10),(0, 0, 0))
#im3 = im1.resize((1000, 1000))
#im3 = im1.rotate(30)
#im3.save('3.jpg')
#print(im1.split())
imfont = ImageFont.truetype(r'C:\windows\Fonts\msyh.ttf', 20)#得用这个才行

#test functions on im1

draw1 = ImageDraw.Draw(im1)
#draw1.arc([(10, 10), (100,200)], 20, 90, 'red')#有效，记得是两个点，这个只有线
#draw1.chord([(10, 10), (200,200)], 20, 110, 'blue', 'black')#有效，注意颜色的使用
#draw1.ellipse([(10,10), (150, 200)], 'blue', 'green')#有效
#draw1.line([(15,200), (210, 5)], 'gray', 20)#这个很简单了
#draw1.pieslice([(10, 5), (100, 99)], 10, 100, 'yellow', 'orange')#区别前面的arc
#draw1.point([(1, 1), (1, 3), (1, 4)], 'black')#有效
#draw1.polygon([(10, 20), (50, 100), (60, 60)], 'purple', 'pink')#多边形
#draw1.rectangle([(10, 10), (150, 150)], 'white', 'red')#参数是对角
draw1.text([10, 10], 'hello', 'red', imfont)
im1.show()
