N, Q = map(int, input().split())
graph = [[False] * N for _ in range(N)]

for _ in range(Q):
    log = list(map(int, input().split()))
    check = log[0]
    a = log[1] - 1
    if check == 1:
        b = log[2] - 1
        graph[a][b] = True
    elif check == 2:
        for i in range(N):
            if i == a:
                continue
            if graph[i][a]:
                graph[a][i] = True
    else:
        xs = []
        for i in range(N):
            if graph[a][i]:
                xs.append(i)
        for x in xs:
            for i in range(N):
                if i == a:
                    continue
                if graph[x][i]:
                    graph[a][i] = True

for i in range(N):
    row = ""
    for j in range(N):
        YN = "N"
        if graph[i][j]:
            YN = "Y"
        row += YN
    print(row)
