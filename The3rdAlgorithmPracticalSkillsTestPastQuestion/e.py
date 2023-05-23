N, M, Q = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

colors = list(map(int, input().split()))
ans = []
for _ in range(Q):
    s = list(map(int, input().split()))
    x = s[1] - 1
    if s[0] == 1:
        ans.append(colors[x])
        for gx in graph[x]:
            colors[gx] = colors[x]
    else:
        y = s[2]
        ans.append(colors[x])
        colors[x] = y

for ai in ans:
    print(ai)
