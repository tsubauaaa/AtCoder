N = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)
C = [0] * N - 1
# 累積和作成
for i in range(N - 1):
    sum_A -= A[i]
    C[i] = sum_A
ans = 0
for i in range(N - 1):
    ans += A[i] * C[i]
    ans %= 10 ** 9 + 7
print(ans)
