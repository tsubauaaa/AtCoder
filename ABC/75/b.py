def create_available_masu(h, w):
    available_masu = []
    for hw in [
        [h - 1, w - 1],
        [h - 1, w],
        [h - 1, w + 1],
        [h, w - 1],
        [h, w + 1],
        [h + 1, w - 1],
        [h + 1, w],
        [h + 1, w + 1],
    ]:
        if hw[0] < 1 or hw[0] > H or hw[1] < 1 or hw[1] > W:
            continue
        available_masu.append(hw)
    return available_masu


H, W = map(int, input().split())
masu = []
for i in range(H):
    masu.append(list(input()))
availables = []

for i in range(1, H + 1):
    for j in range(1, W + 1):
        availables.append(create_available_masu(i, j))
line = []
ans = []
for available in availables:
    cnt = 0
    for a in available:
        if masu[a[0] - 1][a[1] - 1] == "#":
            cnt += 1
    line.append(str(cnt))
    if len(line) == W:
        ans.append("".join(line))
        line = []

for i in range(H):
    for j in range(W):
        if masu[i][j] == "#":
            s = list(ans[i])
            s[j] = "#"
            ans[i] = "".join(s)


for a in ans:
    print(a)
