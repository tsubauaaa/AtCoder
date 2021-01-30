N, M = map(int, input().split())
A = [0] * M
B = [0] * M
for i in range(M):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b
K = int(input())
C = [0] * K
D = [0] * K
for i in range(K):
    c, d = map(int, input().split())
    C[i] = c
    D[i] = d
ans = 0
for i in range(2 ** K):
    dishes = [False] * N
    for j in range(K):
        if (i >> j) & 1:
            dishes[C[j] - 1] = True
        else:
            dishes[D[j] - 1] = True
    tmp = 0
    for a, b in zip(A, B):
        if dishes[a - 1] and dishes[b - 1]:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
