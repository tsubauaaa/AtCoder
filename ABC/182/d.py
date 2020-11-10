N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    print(A[i] * (i + 1))
print(ans)
