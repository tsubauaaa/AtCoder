from fractions import Fraction
import math
from functools import reduce


N, M = map(int, input().split())
A = sorted(map(int, input().split()))

ans = []
if N == 1:
    for k in range(1, M + 1):
        if math.gcd(A[0], k) == 1:
            ans.append(k)
else:
    min_A = A[0] if A[0] != 1 else A[1]
    A_cm = min_A * max(A)
    for k in range(1, M + 1):
        x = Fraction(k, A_cm)
        if str(x) == f"{k}/{A_cm}":
            ans.append(k)

print(len(ans))
for ansi in ans:
    print(ansi)
