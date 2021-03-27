H, W, X, Y = map(int, input().split())
masu = [list(input()) for _ in range(H)]
yoko = masu[X - 1]
tate = []
for m in masu:
    tate.append(m[Y - 1])

ans_t = 0
for i, t in enumerate(tate):
    if i < X - 1:
        if t == "#":
            ans_t = 0
        elif t == ".":
            ans_t += 1
    else:
        if t == "#":
            break
        elif t == ".":
            ans_t += 1

ans_y = 0
for i, y in enumerate(yoko):
    if i < Y - 1:
        if y == "#":
            ans_y = 0
        elif y == ".":
            ans_y += 1
    else:
        if y == "#":
            break
        elif y == ".":
            ans_y += 1
print(ans_t + ans_y - 1)
