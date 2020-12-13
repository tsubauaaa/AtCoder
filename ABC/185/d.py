import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
if M == 0:
    print(1)
    exit()
A.sort()
length = []
before_a = 0
for a in A:
    if a != before_a + 1:
        length.append(a - before_a - 1)
    before_a = a
if N - A[-1] != 0:
    length.append(N - A[-1])

if len(length) == 0:
    print(0)
    exit()

min_l = min(length)
ans = 0
for leng in length:
    if leng == min_l:
        ans += 1
    else:
        ans += math.ceil(leng / min_l)
print(ans)
