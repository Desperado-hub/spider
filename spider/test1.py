from collections import defaultdict

def main():
    # d = defaultdict(list)
    # d['a'].append(1)
    # d['a'].append(1)
    # d['b'].append('sdasd')
    # print(d)

    # d = defaultdict(set)
    # d['a'].add(1)
    # d['a'].add(1)
    # d['a'].add(2)
    # d['b'].add('sdasd')
    # d['b'].add('sdasd')
    # d['b'].add('sdasd12312')
    # print(d)

    # price = {
    #     'acme': 45.23,
    #     'aapl': 612.78,
    #     'ibm': 205.55,
    #     'hpq': 37.20,
    #     'fb': 10.75,
    # }
    # min_price = min(zip(price.values(),price.keys()))
    # print(min_price)

    # a = {
    #     'x': 1,
    #     'y': 2,
    #     'z': 3,
    # }
    # b = {
    #     'x': 11,
    #     'y': 2,
    #     'w': 10,
    # }
    # print(a.keys())
    # print(a.items())
    # print(a.keys()&b.keys())
    # print(a.keys()-b.keys())
    # print(a.items()&b.items())
    # print(a.items()-b.items())

#     items = [1,5,2,1,9,1,5,10]
#     # b = list(1)
#     # b = list(2)
#     # print('b',b)
#     a = list(items)
#     print(a) 
# def dedupe(items):
#     seen = set()
#     for item in items:
#         # if item not in seen:
#         #     yield item
#         seen.add(item)
#         print('seen: ',seen)
#     return 

    # record = '....................100 .......513.25 ..........'
    # SHARES = slice(20, 23)
    # PRICE = slice(31,37)
    # cost = int(record[SHARES])*float(record[PRICE])
    # print(cost)

    dicta = {'key':'142354', 'value': 'nihaiadasd'}
    print(dicta['key'])


if __name__ == "__main__":
    main()