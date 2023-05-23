N, Q = map(int, input().split())
graph = [[False for _ in range(N)] for _ in range(N)]

for i in range(Q):
    S = list(map(int, input().split()))
    a = S[1] - 1
    if S[0] == 1:
        b = S[2] - 1
        graph[a][b] = True
    elif S[0] == 2:
        for i in range(N):
            if i == a:
                continue
            for _ in range(N):
                if graph[i][a]:
                    graph[a][i] = True
    else:
        X = []
        for i in range(N):
            if graph[a][i]:
                X.append(i)
        for x in X:
            for i in range(N):
                if i == a:
                    continue
                if graph[x][i]:
                    graph[a][i] = True
for gi in graph:
    ans = ""
    for gii in gi:
        if gii:
            ans += "Y"
        else:
            ans += "N"
    print(ans)
