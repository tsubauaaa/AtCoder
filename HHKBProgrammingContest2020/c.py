N = int(input())
P = list(map(int, input().split()))
used = [False] * 200000
cur = 0
for i in range(N):
    used[P[i]] = True
    while used[cur]:
        cur += 1
    print(cur)
