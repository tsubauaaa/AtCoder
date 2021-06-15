import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
routes = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    routes[A - 1].append(B - 1)


def dfs(a):
    for b in routes[a]:
        if not check[b]:
            check[b] = True
            dfs(b)


ans = 0
for i in range(N):
    check = [False] * N
    check[i] = True
    dfs(i)
    ans += sum(check)
print(ans)
