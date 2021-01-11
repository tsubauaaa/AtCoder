import math

N, M = map(int, input().split())
x = math.floor(10 ** N / M)
x2 = math.floor(N / math.log10(M))
print(x, x2, x % M, x2 % M)
