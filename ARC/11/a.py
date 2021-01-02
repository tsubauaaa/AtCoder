m, n, N = map(int, input().split())
ans = N
remain = 0
while N >= m:
    remain += N % m
    N = (N - N % m) * n // m
    ans += N
    if N < m:
        N += remain
        remain = 0
print(ans)
