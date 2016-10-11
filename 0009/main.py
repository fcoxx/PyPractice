#!usr/bin/python

from html.parser import HTMLParser

htmpath = r'F:\素材\1.htm'

class aParser(HTMLParser):
    tagp = 0
    currentlink = ''
    linkname = ''
    
    def findhref(self, attrs):
        for attr in attrs:
            if attr[0] == 'href':
                return attr[1]
        return '__def__name__'
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.tagp = 1
            self.currentlink = self.findhref(attrs)
        else:
            self.tagp = 0
            
    def handle_data(self, data):
        if self.tagp == 1:
            self.linkname = data.strip()
            print(self.linkname + ' : ' + self.currentlink)

parser = aParser()

htmcontent = open(htmpath)
htmstr = htmcontent.read()
htmcontent.close()

#print(str(len(htmstr)))

parser.feed(htmstr)
