H, W = map(int, input().split())
masu = []
for _ in range(H):
    m = list(input())
    masu.append(m)
for h in range(H - 1):
    for w in range(W - 1):
        if masu[h][w] == "#":
            if h == 0 and w == 0 and "#" not in (masu[h][w + 1], masu[h + 1][w]):
                print("No")
                exit()
            elif h == 0 and w == W - 1 and "#" not in (masu[h][w - 1], masu[h + 1][w]):
                print("No")
                exit()
            elif h == H - 1 and w == 0 and "#" not in (masu[h - 1][w], masu[h][w + 1]):
                print("No")
                exit()
            elif (
                h == H - 1
                and w == W - 1
                and "#" not in (masu[h - 1][w], masu[h][w - 1])
            ):
                print("No")
                exit()
            elif h == 0 and "#" not in (masu[h][w - 1], masu[h][w + 1], masu[h + 1][w]):
                print("No")
                exit()
            elif h == H - 1 and "#" not in (
                masu[h - 1][w],
                masu[h][w - 1],
                masu[h][w + 1],
            ):
                print("No")
                exit()
            elif w == 0 and "#" not in (masu[h - 1][w], masu[h][w + 1], masu[h + 1][w]):
                print("No")
                exit()
            elif w == W - 1 and "#" not in (
                masu[h - 1][w],
                masu[h][w - 1],
                masu[h + 1][w],
            ):
                print("No")
                exit()
            elif (
                h not in (0, H - 1)
                and w not in (0, W - 1)
                and "#"
                not in (masu[h - 1][w], masu[h][w - 1], masu[h][w + 1], masu[h + 1][w])
            ):
                print("No")
                exit()
            else:
                continue
print("Yes")
