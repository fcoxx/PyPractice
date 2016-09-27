#!usr/bin/python

import random

codeLength = 8              #码的长度
codeNum = 200               #码的个数

tuple0 = []                 #48-57/65-90/97-122
for i in range(0, 123):
    tuple0.append(i)

tupleNum = tuple0[48 : 58]  #数字ascii
tupleCap = tuple0[65 : 91]  #大写字母ascii
tupleSml = tuple0[97 : 123] #小写字母ascii

tuple1 = tupleNum + tupleCap + tupleSml #将需要的ascii存在一个表中
tuple2 = []
for j in tuple1:            #将需要的ascii转换成str
    tuple2.append(chr(j))
    
allCode = []
x = 0
while x < codeNum:
    currentCode = ''
    y = 0
    while y < codeLength:
        currentCode = currentCode + str(random.choice(tuple2))
        y = y + 1
    allCode.append(currentCode)
    x = x + 1
print(allCode)
