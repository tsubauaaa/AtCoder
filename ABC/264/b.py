R, C = map(int, input().split())

grid = []

for i in range(15):
    yoko = []
    for j in range(15):
        if i == 0 or i == 14:
            yoko.append("#")
        elif i == 1 or i == 13:
            if j == 0 or j == 14:
                yoko.append("#")
            else:
                yoko.append(".")
        elif i == 2 or i == 12:
            if j == 1 or j == 13:
                yoko.append(".")
            else:
                yoko.append("#")
        elif i == 3 or i == 11:
            if j in (0, 2, 12, 14):
                yoko.append("#")
            else:
                yoko.append(".")
        elif i == 4 or i == 10:
            if j in (1, 3, 11, 13):
                yoko.append(".")
            else:
                yoko.append("#")
        elif i == 5 or i == 9:
            if j in (0, 2, 4, 10, 12, 14):
                yoko.append("#")
            else:
                yoko.append(".")
        elif i == 6 or i == 8:
            if j in (1, 3, 5, 9, 11, 13):
                yoko.append(".")
            else:
                yoko.append("#")
        else:
            if j in (0, 2, 4, 6, 8, 10, 12, 14):
                yoko.append("#")
            else:
                yoko.append(".")
    grid.append(yoko)


if grid[R - 1][C - 1] == "#":
    print("black")
else:
    print("white")
