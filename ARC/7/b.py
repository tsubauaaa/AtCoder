N, M = map(int, input().split())
ans = [i + 1 for i in range(N)]
now = 0
for _ in range(M):
    nxt = int(input())
    if nxt in ans:
        ans[ans.index(nxt)] = now
    else:
        continue
    now = nxt
for ansi in ans:
    print(ansi)
