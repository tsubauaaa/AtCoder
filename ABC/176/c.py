N = int(input())
A = list(map(int, input().split()))
max_A = max(A)
max_index = A.index(max_A)
ans = 0
for i in range(1, N):
    if i >= max_index:
        ans += max_A - A[i]
    else:
        if A[i - 1] > A[i]:
            ans += A[i - 1] - A[i]
            A[i] = A[i - 1]
print(ans)
