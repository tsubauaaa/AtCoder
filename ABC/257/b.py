N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(Q):
    a = A[L[i] - 1]
    if a == N:
        continue
    else:
        if A.count(a + 1) == 0:
            a += 1
            A[L[i] - 1] = a

print(*A)
