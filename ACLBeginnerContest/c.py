import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
G = {i: [] for i in range(N)}
for i in range(M):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    G[A].append(B)
    G[B].append(A)


def dfs(n):
    visited[n] = True
    for g in G[n]:
        if not visited[g]:
            dfs(g)


ans = 0
visited = [False] * N
for i in range(N):
    if visited[i]:
        continue
    dfs(i)
    ans += 1

print(ans - 1)
