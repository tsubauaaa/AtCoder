from collections import Counter


def comb(n):
    return n * (n - 1) // 2


N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

all_combs = {}
sum_combs = 0
for k, v in C.items():
    all_combs[k] = comb(v)
    sum_combs += all_combs[k]
for i in range(N):
    diff = all_combs[A[i]] - comb(C[A[i]] - 1)
    print(sum_combs - diff)
