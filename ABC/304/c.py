import sys

sys.setrecursionlimit(1000000)

N, D = map(int, input().split())
XY = []
for i in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])

virused = [False] * N


def dfs(x1, y1):
    for i, xy in enumerate(XY):
        if virused[i]:
            continue
        x2, y2 = xy[0], xy[1]
        d = (x1-x2)**2 + (y1-y2)**2
        if D*D >= d:
            virused[i] = True
            dfs(x2, y2)


dfs(XY[0][0], XY[0][1])

for v in virused:
    if v:
        print("Yes")
    else:
        print("No")
