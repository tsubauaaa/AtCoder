N, M = map(int, input().split())
A = list(map(int, input().split()))
sum_A = sum(A)
ans = 0
for i in range(N):
    if A[i] >= sum_A / (4 * M):
        ans += 1
print("Yes" if M <= ans else "No")
