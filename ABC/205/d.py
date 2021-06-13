
def check(n):
    if n in A:
        return check(n + 1)
    else:
        return n


N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = [int(input()) for _ in range(Q)]
max_A = max(A)

ans = []
for i in range(Q):
    if K[i] in A:
        index = A.index(K[i])
        a = check(K[i] + 1)
        a += index
    else:
        if K[i] > max_A:
            a = K[i] + N
        else:
            a = K[i]
    ans.append(a)

for ansi in ans:
    print(ansi)
