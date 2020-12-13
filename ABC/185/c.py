from functools import reduce
from operator import mul


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


L = int(input())
print(combinations_count(L - 1, 11))
