import math


def lcm(a, b):
    return a * b / math.gcd(a, b)


A, B = map(int, input().split())
print(int(lcm(A, B)))
