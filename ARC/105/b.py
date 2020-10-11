N = int(input())
aaa = list(map(int, input().split()))
aaa = [min(aaa), sorted(aaa)[-2], max(aaa)]

while True:
    # print(aaa)
    x = min(aaa)
    X = max(aaa)
    xx = aaa[-2]
    aaa = [x, xx, X]
    if x != X:
        aaa = [x, xx, X - x]
    else:
        break

print(aaa[0])
