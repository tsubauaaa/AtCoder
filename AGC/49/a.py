def dfs(cnt, tmp, indexes):
    if cnt == N:
        return
    cnt += 1
    for index in indexes:
        tmp[index] = 0
        dfs(cnt, tmp, [n for n, v in enumerate(graph[index]) if v == "1"])


N = int(input())
graph = [input() for _ in range(N)]
removes = [0] * N
ans = 0
for i in range(N):
    tmp = [1] * N
    tmp[i] = 0
    dfs(0, tmp, [n for n, v in enumerate(graph[i]) if v == "1"])
    if sum(tmp) == 0:
        ans += 1
    else:
        ans += tmp.count(1) + 1
print(ans / N)
