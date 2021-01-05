import math

N = int(input())
A = list(map(int, input().split()))
sum_b = 0
ans = 0
for a in A:
    if a != 0:
        sum_b += 1
        ans += a
print(math.ceil(ans / sum_b) if sum_b != 0 else 0)
