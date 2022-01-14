N, M = map(int, input().split())

A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

cnt = 0
for i in range(N - M + 1):
    for j in range(N - M + 1):
        target = [a[i : i + M] for a in A][j : j + M]
        if target == B:
            print("Yes")
            exit()
print("No")
