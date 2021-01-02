H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
min_A = 100
for i in range(H):
    tmp_min_A = min(A[i])
    min_A = min(min_A, tmp_min_A)
ans = 0
for i in range(H):
    for j in range(W):
        ans += A[i][j] - min_A
print(ans)
