N, A, B = map(int, input().split())

init_tile = []
init_tile_rev = []
for i in range(A):
    init_tile.append("." * B)
    init_tile_rev.append("#" * B)

init_tiles = []
init_tiles_rev = []

for i in range(A):
    tmp = ""
    tmp_rev = ""
    for j in range(N):
        if j % 2 == 0:
            tmp += init_tile[i]
            tmp_rev += init_tile_rev[i]
        else:
            tmp += init_tile_rev[i]
            tmp_rev += init_tile[i]
    init_tiles.append(tmp)
    init_tiles_rev.append(tmp_rev)


for i in range(N):
    if i % 2 == 0:
        for t in init_tiles:
            print(t)
    else:
        for t in init_tiles_rev:
            print(t)

