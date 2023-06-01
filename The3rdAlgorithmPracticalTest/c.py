A, R, N = map(int, input().split())

if R == 1:
    print(A)
    exit()

for i in range(1, N+1):
    item = A * R ** (i-1)
    if item > 10 ** 9:
        print("large")
        exit()

print(item)
