import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]


def dfs(x, y):
    if not (0 <= x < H) or not (0 <= y < W) or c[x][y] == "#":
        return
    if c[x][y] == "g":
        print("Yes")
        exit()

    c[x][y] = "#"
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            sx = i
            sy = j
dfs(sx, sy)
print('No')
