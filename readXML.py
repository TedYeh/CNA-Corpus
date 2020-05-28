from html.parser import HTMLParser 
from re import sub 
from sys import stderr 
from traceback import print_exc 
 
class _DeHTMLParser(HTMLParser): 
    def __init__(self): 
        HTMLParser.__init__(self) 
        self.__text = [] 
        self.__isStory = False
 
    def handle_data(self, data): 
        if self.__isStory:
            text = data.strip() 
            if len(text) > 0: 
                text = sub('[(a-zA-Z)]+', '', text) 
                self.__text.append(text + ' ')  
 
    def handle_starttag(self, tag, attrs):
        if tag == 'doc':
            for name,value in attrs:
                if name == 'type' and value == 'story':
                    self.__isStory = True  
        if tag == 'p': 
            self.__text.append('\n\n') 
        elif tag == 'br': 
            self.__text.append('\n') 
    
    def handle_endtag(self,tag):
        if tag == 'doc':
            self.__isStory = False

    def handle_startendtag(self, tag, attrs): 
        if tag == 'br': 
            self.__text.append('\n\n') 
 
    def text(self): 
        return ''.join(self.__text).strip() 
 
 
def dehtml(text): 
    try: 
        parser = _DeHTMLParser() 
        parser.feed(text) 
        parser.close() 
        return parser.text() 
    except: 
        print_exc(file=stderr) 
        return text 
 
 
def main(): 
    with open('cna_cmn_199101','r',encoding='utf-8') as f:
        s = f.read()        
        with open('test.txt','w') as f:
            f.write(dehtml(s))
 
 
if __name__ == '__main__': 
    main()
