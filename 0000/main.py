#!/usr/bin/python

from PIL import Image
from PIL import ImageFont

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
ImageFont imfont = ImageFont.truetype()
