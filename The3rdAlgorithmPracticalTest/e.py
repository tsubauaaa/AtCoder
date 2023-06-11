N, M, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

colors = list(map(int, input().split()))
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    first = query[0]
    x = query[1] - 1
    color = colors[x]
    ans.append(color)
    if first == 1:
        for p in graph[x]:
            colors[p] = color
    else:
        y = query[2]
        colors[x] = y

for ansi in ans:
    print(ansi)
