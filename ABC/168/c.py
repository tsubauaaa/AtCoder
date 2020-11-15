import math

A, B, H, M = map(int, input().split())

short_rad = H * (360 / 12) + M * 0.5
long_rad = M * (360 / 60)
rad = abs(short_rad - long_rad)
print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(rad))))
