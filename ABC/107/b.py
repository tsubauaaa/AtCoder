H, W = map(int, input().split())
masu = [list(input()) for _ in range(H)]

for w in range(W):
    cnt = 0
    for h in range(H):
        if masu[h][w] == ".":
            cnt += 1
    if cnt == H:
        for h in range(H):
            masu[h][w] = "0"
for h in range(H):
    cnt = 0
    for w in range(W):
        if masu[h][w] in (".", "0"):
            cnt += 1
    if cnt == W:
        for w in range(W):
            masu[h][w] = "0"

for h in range(H):
    for w in range(W):
        if masu[h][w] != "0":
            print(masu[h][w], end="")
    print("\n", end="")
