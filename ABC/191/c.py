def check_square(i, j):
    d_cnt = 0
    for h in (-1, 0, 1):
        for w in (-1, 0, 1):
            if masu[i][j] != "#":
                continue
            if masu[i + h][j + w] == ".":
                d_cnt += 1
    if d_cnt >= 4:
        return True
    else:
        return False


H, W = map(int, input().split())
masu = []
for i in range(H):
    masu.append(list(input()))
square = 0
for i in range(1, H - 1):
    for j in range(1, W - 1):
        if check_square(i, j):
            square += 1
print(square)
