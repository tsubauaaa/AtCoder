import math

H = int(input())
W = int(input())
N = int(input())

M = H * W

print(math.ceil(min(N / H, N / W)))
