import itertools

N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b
ans = 10 ** 5 + 1
for i in range(N):
    for j in range(N):
        if i != j:
            tmp = max(A[i], B[j])
        else:
            tmp = A[i] + B[j]
        ans = min(ans, tmp)

print(ans)
