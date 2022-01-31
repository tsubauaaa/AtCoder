H, W = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(H)]
tr = []
for i in range(W):
    tr_row = []
    for vector in M:
        tr_row.append(vector[i])
    tr.append(tr_row)

for tri in tr:
    print(*tri)
