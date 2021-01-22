a, b = map(int, input().split())
d = b - a
towers = [0] * 1000
for i in range(1, 1000):
    towers[i - 1] = i * (i + 1) // 2
for i in range(1, 1000):
    if towers[i] - towers[i - 1] == d:
        print(towers[i - 1] - a)
        exit()
