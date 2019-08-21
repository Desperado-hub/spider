import requests
from bs4 import BeautifulSoup
import lxml
import time
import fnmatch
import random

class spiderforwiki(object):
    def __init__(self,url):
        self.url = url
    
    def parseUrl(self):
        time.sleep(random.random() * 10)
        header = self.getHeader()
        page = requests.get(self.url,header)
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, "html.parser")	
        return soup
    
    def parseText(self,soup):
        contents = []
        soup = soup.find(id='bodyContent')
        soup = soup.find(id='mw-content-text')
        soup = soup.findAll('li',{'class':'mw-search-result'})
        for li in soup:
            a = li.find('a')['title']
            print(a)
            contents.append(a)
        return contents

    def savecontent(self,content):
        filename = "/Users/czy/Documents/Projects/spider/content.txt"
        f =open(filename, "a")
        for value in content:
            f.write('\'' + value + '\'' + ',') 
        f.close

    def getHeader(self):
        headers = [
            # {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'},
            # {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
            # {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
            # {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
            # {'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'},
            # {'User-Agent': 'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'},
            # {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'},
            # {'User-Agent': 'Mozilla/5.0 (Linux; U; android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
            # {'User-Agent': 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+'},
            # {'User-Agent': 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124'},
        ]
        # header = headers[random.randint(0,10)]
        header = headers[0]
        return header