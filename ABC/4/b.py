masu = []
for i in range(4):
    masu.append(list(map(str, input().split())))
masu_conv = []
for i in range(3, -1, -1):
    line = []
    for j in range(3, -1, -1):
        line.append(masu[i][j])
    masu_conv.append(line)
print("\n".join(" ".join([j for j in i]) for i in masu_conv))
