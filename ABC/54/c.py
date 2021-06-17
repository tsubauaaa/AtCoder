
import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]


def dfs(i, check):
    if False not in check:
        return 1
    ans = 0
    for p in graph[i]:
        if not check[p]:
            check[p] = True
            ans += dfs(p, check)
            check[p] = False
    return ans


for i in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    if a != 1:
        graph[b - 1].append(a - 1)

check = [False] * N
check[0] = True
print(dfs(0, check))
