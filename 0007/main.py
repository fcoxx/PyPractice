#!usr/bin/python

import os

dirpath = r'E:\WORK\160831_数据处理\正式程序'

filelist = os.listdir(dirpath)

allspacelines = 0
allnonspacelines = 0
for filename in filelist:
    spacelines = 0
    nonspacelines = 0
    if filename.split('.')[1] != 'm':   #跳过非源码文件
        #print(filename)
        continue

    filepath = dirpath + '\\' + filename

    currentfile = open(filepath)

    lines = currentfile.readlines()
    #print(filelines)

    for line in lines:
        line0space = line.strip()
        if line0space == '':
            spacelines = spacelines + 1
        else:
            nonspacelines = nonspacelines + 1
    
    currentfile.close()

    print('current file:' + filepath)
    print('space lines:' + str(spacelines))
    print('nonspace lines:' + str(nonspacelines))
    print('------------------------------')
    
    allspacelines = allspacelines + spacelines
    allnonspacelines = allnonspacelines + nonspacelines
    #break
    
print('all space lines:' + str(allspacelines))
print('all nonspace lines:' + str(allnonspacelines))
