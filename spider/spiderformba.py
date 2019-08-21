import requests
from bs4 import BeautifulSoup
import lxml
import time
import fnmatch
import random

class spiderformba(object):
    def __init__(self,url):
        self.url = url
    
    def parseUrl(self):
        header = self.getHeader()
        page = requests.get(self.url,header)
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, "html.parser")	
        return soup

    # 二级parse URL
    def parseUrlinnner(self,url):
        time.sleep(random.random() * 10)
        header = self.getHeader()
        page = requests.get(url,header)
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, "html.parser")	
        return soup
    
    def parseText(self,soup):
        url = []
        contents = []
        soup = soup.find(id='globalWrapper')
        soup = soup.find(id = 'search-result')
        soup = soup.find('table')
        for tr in soup:
            a = tr.find('a').text.strip()
            contents.append(a)
            if (a.find('王八蛋') != -1): #or (a.find('集团') != -1) or (a.find('公司') != -1): # or fnmatch(a,'company') or fnmatch(a,'COMPANY') 
                print(a)
                soup1 = self.parseUrlinnner('https://wiki.mbalib.com/wiki/' + a)
                soup1 = soup1.find(id = 'globalWrapper')
                soup1 = soup1.find(id = 'column-content')
                soup1 = soup1.find(id = 'content')
                soup1 = soup1.find(id = 'bodyContent')
                soup1 = soup1.find(rel = 'nofollow')
                print(soup1)    
                try:
                    url.append(soup1.text.strip())
                except:
                    print('noAttribute')
                    continue
        return contents,url

    def saveurl(self,url):
        if url != None:
            filename = "url.txt"
            f =open(filename, "a")
            for value in url:
                f.write('\'' + value + '\'' + ',') 
            f.close
        

    def savecontent(self,content):
        filename = "content.txt"
        f =open(filename, "a")
        for value in content:
            f.write('\'' + value + '\'' + ',') 
        f.close

    def getHeader(self):
        headers = [
            # {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
            # {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
            # {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
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