N = int(input())

res = [0] * (N + 1)
for x in range(1, int(N ** 0.5) + 1):
    for y in range(1, int(N ** 0.5) + 1):
        for z in range(1, int(N ** 0.5) + 1):
            if x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x > N:
                break
            res[x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x] += 1
for i in range(1, N + 1):
    print(res[i])
