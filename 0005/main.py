#!usr/bin/python

import os
from PIL import Image

picpath = r'F:\图片'
ipheight = 1136
ipwidth = 640

filelist = os.listdir(picpath)

for filename in filelist:
    namesect = filename.split('.')
    newfilename = namesect[0] + '__.' + namesect[1] #新的文件名
    newfilepath = picpath + '\\' + newfilename
    
    filepath = picpath + '\\' + filename
    image = Image.open(filepath)
    picheight = image.size[0]
    picwidth = image.size[1]    #图片的原始大小

    Hfactor = 1
    if picheight > ipheight:
        Hfactor = picheight / ipheight

    Vfactor = 1
    if picwidth > ipwidth:
        Vfactor = picwidth / ipwidth

    if Hfactor > Vfactor:
        factor = Hfactor
    else:
        factor = Vfactor

    if factor < 1:
        factor = 1  #防止图片被放大

###这里要注意的是，取整除法中，如果俩数中有一个是浮点数，那么结果将是个取了整的浮点数
    newsize = (int(picheight // factor), int(picwidth // factor))

    newimage = image.resize(newsize)

    newimage.save(newfilepath)
    print('current image:' + filepath)
    print('before:' +  str(picheight) + '*' + str(picwidth))
    print('after:' + str(newsize[0]) + '*' + str(newsize[1]))
    print('save :' + newfilepath)
    print('--------------------------')
