dices=list(map(int,input().split()))

matches = [0]*3
for i in range(3):
    matches[i] = dices.count(dices[i])

if len(list(set(matches))) == 1:
    if matches[0] == 1:
        print(0)
    else:
        print(dices[0])
else:
    print(dices[matches.index(1)])