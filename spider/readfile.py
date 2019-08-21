import re

def main():
    print('begin to process')
    filename1 = "/Users/czy/Documents/Projects/spider/content.txt"
    filename2 = "/Users/czy/Documents/Projects/spider/sort.txt"
    f1 = open(filename1,'r')
    f2 = open(filename2,'a')
    s = f1.read()
    arr = s.split(',')
    i = 0
    for str1 in arr:
        # print(str1,type(str1))
        if str1.find('List') > -1:
            str1 = str1.replace('List of ','')
            print(str1)
            # continue
        f2.write(str1 + ',')
        i = i + 1
    f1.close()
    f2.close()
    print('work finished')


if __name__ == "__main__":
    main()