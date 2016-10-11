#!usr/bin/python

from html.parser import HTMLParser

htmpath = r'F:\素材\1.htm'

class aParser(HTMLParser):
    tagp = 0
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.tagp = 1
        else:
            self.tagp = 0
            
    def handle_data(self, data):
        if self.tagp == 1:
            if data.strip() != '':
                print('-:' + data)

parser = aParser()

htmcontent = open(htmpath)
htmstr = htmcontent.read()
htmcontent.close()

#print(str(len(htmstr)))

parser.feed(htmstr)
