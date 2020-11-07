N = int(input())
A = list(map(int, input().split()))
sum_start = 0
sum_end = sum(A)
ans = 2020202020
for i in range(N):
    sum_start += A[i]
    sum_end -= A[i]
    ans = min(ans, abs(sum_start - sum_end))

print(ans)
