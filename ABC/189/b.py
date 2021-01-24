N, X = map(int, input().split())
ans = N + 2
Y = 100 * X
for i in range(N):
    V, P = map(int, input().split())
    Y -= V * P
    if Y < 0 and ans == N + 2:
        ans = i + 1
print(-1 if ans == N + 2 else ans)
