N, K = map(int, input().split())
ans = 10 ** 5 + 1
for i in range(N):
    a = int(input())
    K -= a
    if K <= 0:
        ans = min(ans, i + 1)
print(ans)
