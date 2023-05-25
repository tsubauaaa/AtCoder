import sys

sys.setrecursionlimit(10**9)

K = int(input())

ans = []


def dfs(n):
    if n > 3234566667:
        return
    m = n % 10
    global ans

    ans.append(n)

    if m == 0:
        dfs(10 * n + m)
        dfs(10 * n + m + 1)
    elif 1 <= m <= 8:
        dfs(10 * n + m)
        dfs(10 * n + m + 1)
        dfs(10 * n + m - 1)
    elif m == 9:
        dfs(10 * n + m)
        dfs(10 * n + m - 1)


for i in range(1, 10):
    dfs(i)

ans.sort()
print(ans[K-1])
