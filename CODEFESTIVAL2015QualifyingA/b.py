N = int(input())
A = list(map(int, input().split()))
ans = A[0]
for i in range(1, N):
    tmp = ans
    ans = A[i] + ans * 2
print(ans)
