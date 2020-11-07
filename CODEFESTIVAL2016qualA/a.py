N = int(input())
A = list(map(int, input().split()))
R = [i for i in range(1, N + 1)]
ans = 0
for i in range(N):
    if A[R[A[i] - 1] - 1] == i + 1:
        ans += 1

print(ans // 2)
