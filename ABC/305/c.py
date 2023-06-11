H, W = map(int, input().split())
masu = []
max_target = 0
start_target = W
for i in range(H):
    row = input()
    cnt = row.count("#")
    max_target = max(max_target, cnt)
    masu.append(row)
    for j in range(W):
        if row[j] == "#":
            start_target = min(start_target, j)

for h, row in enumerate(masu):
    if row.count(".") == W:
        continue
    for w in range(start_target, start_target+max_target):
        if row[w] == ".":
            print(h+1, w+1)
            break
