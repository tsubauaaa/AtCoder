N,K=map(int,input().split())

targets = {}
for i in range(N):
    v, m = map(int,input().split())
    if targets.get(v):
        targets[v] += m
    else:
        targets[v] = m
sorted_targets = sorted(targets.items(), key=lambda x:x[0])
ans = 0
for v,m in sorted_targets:
    K -= (v-ans)
    if K >= 0:
        K += m
        ans = v
    else:
        K += (v-ans)
        break
print(ans+K)