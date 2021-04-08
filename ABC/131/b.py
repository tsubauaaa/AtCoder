N, L = map(int, input().split())
taste = [0] * N
min_index = 0
for i in range(1, N + 1):
    taste[i - 1] = L + i - 1
    if 1 < i < N + 1 and abs(taste[i - 1]) < abs(taste[i - 2]):
        min_index = i - 1
print(sum(taste) - taste[min_index])
