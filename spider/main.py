from spiderformba import spiderformba
from spiderforwiki import spiderforwiki
import time
import random

def main():
    
    print("circle begin...")
    search = '金融'
    a = 0
    for i in range(74):
        print(f'开始第{i+1}圈循环')
        # url = f'https://wiki.mbalib.com/w/index.php?title=Special:Search&limit=20&offset={a}&ns0=1&redirs=1&searchx=1&search=' # 这是mbalib的爬取
        url = f'https://wiki.mbalib.com/w/index.php?title=Special:Search&limit=20&offset={a}&ns0=1&redirs=1&searchx=1&search={search}' # 这是mbalib的爬取
        # url = f'https://en.wikipedia.org/w/index.php?title=Special:Search&limit=20&offset=0&profile=default&search=list+of+telecommunication+industry+intitle%3Atelecommunication&advancedSearch-current={{%22fields%22:{{%22intitle%22:%22telecommunication%22}}}}&ns0=1'
        # url = f'https://en.wikipedia.org/w/index.php?title=Special:Search&limit=20&offset={a}&ns0=1&search=list+of+electric+industry&advancedSearch-current={{}}'
        # url = f'https://en.wikipedia.org/w/index.php?title=Special:Search&limit=20&offset={a}&ns0=1&search=list+of+telecom+term&advancedSearch-current={{}}'
        spider1 = spiderformba(url)
        soup = spider1.parseUrl()
        content,url1 = spider1.parseText(soup)
        spider1.savecontent(content)
        spider1.saveurl(url1)
        a = 20 + a
        time.sleep(30 + random.random() * 10)
        

if __name__ == "__main__":
    main()
