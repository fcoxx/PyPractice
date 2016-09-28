#!usr/bin/python

filePath = 'article.txt'

file = open(filePath)

articleString = file.read()     #保存全部为一个字符串
articleString1 = articleString.replace(',', ' ')    #去逗号
articleString2 = articleString1.replace('.', ' ')   #取句号
words = articleString2.split(' ')   #用空格拆分成单词

wordsDict = {}
for word in words:
    if word in wordsDict:
        wordsDict[word] = wordsDict.get(word) + 1
    else:
        wordsDict[word] = 1
print(wordsDict)



