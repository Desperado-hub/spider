from spider import spider
import time

def main():
    
    print("circle begin...")
    a = 0
    for i in range(20):
        print(f'开始第{i}圈循环')
        url = f'https://wiki.mbalib.com/w/index.php?title=Special:Search&limit=20&offset={a}&ns0=1&redirs=1&searchx=1&search=电力'
        spider1 = spider(url)
        try:
            soup = spider1.parseUrl()
        except BaseException:
            continue
        content,url1 = spider1.parseText(soup)
        spider1.savecontent(content)
        spider1.saveurl(url1)
        # print(content,'\n')
        # print(url1,'\n')
        a = 20 + i*20
        time.sleep(10)
        

if __name__ == "__main__":
    main()
