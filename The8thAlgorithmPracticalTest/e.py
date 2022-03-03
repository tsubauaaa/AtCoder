N, K = map(int, input().split())
c = list(map(int, input().split()))
p = list(map(int, input().split()))

cp = {}
for ci, pi in zip(c, p):
    if ci in cp:
        if cp[ci] > pi:
            cp[ci] = pi
    else:
        cp[ci] = pi

if len(cp) < K:
    print(-1)
    exit()

sorted_cp = sorted(cp.items(), key=lambda x: x[1])

ans = 0
for i in range(K):
    ans += sorted_cp[i][1]

print(ans)
