N, Y = map(int, input().split())
for x in range(N + 1):
    for y in range(N + 1):
        z = N - x - y
        if z < 0:
            break
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print(f"{x} {y} {z}")
            exit()
print("-1 -1 -1")
