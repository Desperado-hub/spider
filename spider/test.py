from collections import Counter
from operator import itemgetter

def main():
    # words = [
    # 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    # 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    # 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    # 'my', 'eyes', "you're", 'under'
    # ]
    # counts = Counter(words)
    # top = counts.most_common(3)
    # print(top)

    rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    # group_byfnane = sorted(rows,key=itemgetter('fname'))
    # group_byuid = sorted(rows,key=itemgetter('uid'))
    # print(group_byfnane)
    # print(group_byuid)

    print([n for n in rows])

if __name__ == "__main__":
    main()