N = int(input())
P = list(map(int, input().split()))

ancestor = {1: 0}

for i in range(N - 1):
    ancestor[i + 2] = P[i]

next = N
ans = 0
while True:
    next = ancestor[next]
    if next == 0:
        print(ans)
        exit()
    ans += 1
