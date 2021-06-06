x, y = map(int, input().split())
hands = [False] * 3

if x == y:
    print(x)
else:
    for z in (x, y):
        hands[z] = True
    for i in range(3):
        if not hands[i]:
            print(i)
