import math

a, b, d = map(int, input().split())

rad = math.radians(d)

print(math.cos(rad) * a - math.sin(rad) * b, math.sin(rad) * a + math.cos(rad) * b)

