n, m = map(int, input().split())

h = n if 12 > n else n - 12

angle = abs(h * 30 - m * 5.5)

print(min(angle, 360 - angle))
