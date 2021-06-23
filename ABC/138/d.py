import sys
sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
graph = {i + 1: [] for i in range(N)}
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
points = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    points[p - 1] += x


def dfs(now, prev=-1):
    for next in graph[now]:
        if next == prev:
            continue
        points[next - 1] += points[now - 1]
        dfs(next, now)


dfs(1)
print(*points)
