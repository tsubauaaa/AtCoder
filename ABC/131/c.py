import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


A, B, C, D = map(int, input().split())
B_meet = B - (B // C + B // D - B // lcm(C, D))
A_meet = (A - 1) - ((A - 1) // C + (A - 1) // D - (A - 1) // lcm(C, D))
print(B_meet - A_meet)
