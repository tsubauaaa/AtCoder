import math
from itertools import combinations

ans = 0
A, B = map(int, input().split())
nums = [i for i in range(A, B + 1)]
ans = 0
target = B // 2
for i in range(B, A - 1, -1):
    print(i)
