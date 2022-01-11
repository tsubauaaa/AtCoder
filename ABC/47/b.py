W, H, N = map(int, input().split())
area = []
for i in range(H):
    area.append(list("." * W))

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(H):
            for j in range(x):
                area[i][j] = "#"
    elif a == 2:
        for i in range(H):
            for j in range(x, W):
                area[i][j] = "#"
    elif a == 3:
        for i in range(y):
            area[i] = list("#" * W)
    else:
        for i in range(y, H):
            area[i] = list("#" * W)
ans = 0
for a in area:
    ans += a.count(".")

print(ans)
