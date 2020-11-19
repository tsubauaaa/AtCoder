money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)

for i in range(2 ** n):
    bag = []
    buy = 0
    for j in range(n):
        if (i >> j) & 1:
            bag.append(item[j][0])
            buy += item[j][1]
    if buy <= money:
        print(buy, bag)
