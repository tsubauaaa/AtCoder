x1, y1, x2, y2 = map(int, input().split())

points1 = [
    (x1 - 2, y1 + 1),
    (x1 - 1, y1 + 2),
    (x1 + 1, y1 + 2),
    (x1 + 2, y1 + 1),
    (x1 + 2, y1 - 1),
    (x1 + 1, y1 - 2),
    (x1 - 1, y1 - 2),
    (x1 - 2, y1 - 1),
]

points2 = [
    (x2 - 2, y2 + 1),
    (x2 - 1, y2 + 2),
    (x2 + 1, y2 + 2),
    (x2 + 2, y2 + 1),
    (x2 + 2, y2 - 1),
    (x2 + 1, y2 - 2),
    (x2 - 1, y2 - 2),
    (x2 - 2, y2 - 1),
]

for p1 in points1:
    for p2 in points2:
        if p1[0] == p2[0] and p1[1] == p2[1]:
            print("Yes")
            exit()
print("No")
