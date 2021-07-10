N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = "Yes"
for i in range(1, N + 1):
    if i % 2 == 0:
        X -= A[i - 1] - 1
    else:
        X -= A[i - 1]
    if X < 0:
        ans = "No"
print(ans)
