N, M = map(int, input().split())
bulbs = [0] * M
for i in range(M):
    ks = list(map(int, input().split()))
    bulbs[i] = ks[1:]
ps = list(map(int, input().split()))
ans = 0
for i in range(2 ** N):
    bulb_on = 0
    onoff = [False] * N
    for j in range(N):
        if (i >> j) & 1:
            onoff[j] = True
    for switches, p in zip(bulbs, ps):
        sw_on = 0
        for switche in switches:
            if onoff[switche - 1]:
                sw_on += 1
        if sw_on % 2 == p:
            bulb_on += 1
    if bulb_on == M:
        ans += 1
print(ans)
