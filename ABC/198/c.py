import math

R, X, Y = map(int, input().split())

d = math.sqrt(X ** 2 + Y ** 2)
ans = 0
if R > d:
    ans = 2
else:
    ans = math.ceil(d / R)
print(ans)
