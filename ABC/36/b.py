N = int(input())
masu = [list(input()) for _ in range(N)]
for i in range(N):
    if i > 0:
        print("\n", end="")
    for j in range(N - 1, -1, -1):
        print(masu[j][i], end="")
