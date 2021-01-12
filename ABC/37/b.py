N, Q = map(int, input().split())
ans = [0] * N
for i in range(Q):
    L, R, T = map(int, input().split())
    for j in range(L - 1, R):
        ans[j] = T
for ansi in ans:
    print(ansi)
