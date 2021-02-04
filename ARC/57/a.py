A, K = map(int, input().split())
if K == 0:
    print(2 * 10 ** 12 - A)
    exit()
i = 0
while A < 2 * 10 ** 12:
    A += 1 + K * A
    i += 1
print(i)
