import math

N = int(input())
X = list(map(int, input().split()))
m = 0
u = 0
c = 0

for i in range(N):
    m += abs(X[i])
    u += abs(X[i]) ** 2
    c = max(c, abs(X[i]))


print(m)
print(math.sqrt(u))
print(c)
