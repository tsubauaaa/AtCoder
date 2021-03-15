import itertools
import math

N = int(input())
X = list(map(int, input().split()))

primes = []
for i in range(2, 50):
    for j in range(2, 51):
        if i % j == 0:
            break
    if i == j:
        primes.append(i)

for i in range(1, 16):
    for combs in itertools.combinations(primes, i):
        y = 1
        for comb in combs:
            y *= comb
        ans = [1] * N
        for j in range(N):
            if math.gcd(X[j], y) != 1:
                ans[j] = 0
        if sum(ans) == 0:
            print(y)
            exit()
