N, Q = map(int, input().split())
a = list(map(int, input().split()))

memo = {}

for i in range(N):
    if a[i] not in memo:
        memo[a[i]] = [i]
    else:
        memo[a[i]].append(i)
ans = []
for i in range(Q):
    x, k = map(int, input().split())
    if x in memo and len(memo[x]) >= k:
        ans.append(memo[x][k - 1] + 1)
    else:
        ans.append(-1)

print("\n".join(map(str, ans)))
