import requests
from bs4 import BeautifulSoup
import lxml
import time
import fnmatch

class spider(object):
    def __init__(self,url):
        self.url = url
    
    def parseUrl(self):
        headers = {
            'User-Agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        try:
            page = requests.get(self.url,headers,timeout=5)
        except:
            return None
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, "html.parser")	
        return soup

    # 二级parse URL
    def parseUrlinnner(self,url):
        headers = {
            'User-Agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        try:
            page = requests.get(self.url,headers,timeout=5)
        except:
            return None
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
            if (a.find('公司') != -1) or (a.find('集团') != -1): # or fnmatch(a,'company') or fnmatch(a,'COMPANY') 
                soup1 = self.parseUrlinnner('https://wiki.mbalib.com/wiki/' + a)
                if soup1 != None:
                    soup1 = soup1.find(id='globalWrapper')
                    soup1 = soup1.find(id='column-content')
                    soup1 = soup1.find(id='content')
                    soup1 = soup1.find(target='_blank')
                    if soup1 != None:
                        url.append(soup1.text.strip())
                    else:
                        pass
        return contents,url

    def saveurl(self,url):
        if url != None:
            filename = "/Users/czy/Documents/Projects/spider/url.txt"
            f =open(filename, "a")
            for value in url:
                f.write('\'' + value + '\'' + ',') 
            f.close
        

    def savecontent(self,content):
        filename = "/Users/czy/Documents/Projects/spider/content.txt"
        f =open(filename, "a")
        for value in content:
            f.write('\'' + value + '\'' + ',') 
        f.close