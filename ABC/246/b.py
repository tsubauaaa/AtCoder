import math

# for A in range(1, 1001):
#     for B in range(1, 1001):
#         a = B / A
#         b = 0

#         x = math.sqrt(1 / (1 + a ** 2))
#         y = a * x

#         print(x, y)

A, B = map(int, input().split())
if A == 0:
    print(0, 1)
    exit()
a = B / A
b = 0

x = math.sqrt(1 / (1 + a ** 2))
y = a * x

print(x, y)
