N = int(input())
M = 0
i = 1
while M < N:
    M = i * (i + 1) // 2
    i += 1
print(i - 1)
