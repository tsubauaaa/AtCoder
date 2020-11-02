import math
from functools import reduce

N = int(input())
a = list(map(int, input().split()))


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def f(m):
    y = 0
    for i in range(N):
        y += m % a[i]
    return y


lcm = lcm(*a)
print(f(lcm - 1))
