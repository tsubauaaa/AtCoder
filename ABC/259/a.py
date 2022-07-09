N, M, X, T, D = map(int, input().split())
ans = T
for i in range(N, M - 1, -1):
    if X <= i <= N:
        continue
    ans -= D

print(ans)