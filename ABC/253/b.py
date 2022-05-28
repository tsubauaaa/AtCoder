H, W = map(int, input().split())
masu = [list(input()) for _ in range(H)]
koma = []

for h in range(H):
    for w in range(W):
        if masu[h][w] == "o":
            koma.append([h, w])

print(abs(koma[0][0] - koma[1][0]) + abs(koma[0][1] - koma[1][1]))
