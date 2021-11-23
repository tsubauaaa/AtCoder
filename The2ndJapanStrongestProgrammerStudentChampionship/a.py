import math

X, Y, Z = map(int, input().split())
W = Z*Y/X

print(math.ceil(W-1))
