import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]

distances = []

for a in A:
    tmp = []
    for i in range(N):
        if i + 1 in A:
            continue
        tmp.append(
            math.sqrt((XY[a - 1][0] - XY[i][0]) ** 2 + (XY[a - 1][1] - XY[i][1]) ** 2)
        )
    distances.append(tmp)

distances = list(zip(*distances))

ans = []
for d in distances:
    ans.append(min(d))

print(max(ans))

