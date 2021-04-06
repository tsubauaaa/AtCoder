N = int(input())
W = list(map(int, input().split()))
ans = 10001
for i in range(1, N):
    tmp = abs(sum(W[:i]) - sum(W[i:]))
    ans = min(ans, tmp)
print(ans)
