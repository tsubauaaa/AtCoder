import math

a = int(input())
b = int(input())
n = int(input())

lcm = a * b // math.gcd(a, b)

for i in range(n, 40000):
    if i % lcm == 0:
        print(i)
        exit()
