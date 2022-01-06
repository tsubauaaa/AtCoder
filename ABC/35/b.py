S = list(input())
T = int(input())

S.sort(reverse=True)
pos = (0, 0)

for s in S:
    if s == "U":
        pos = (pos[0], pos[1] + 1)
    elif s == "D":
        pos = (pos[0], pos[1] - 1)
    elif s == "L":
        pos = (pos[0] - 1, pos[1])
    elif s == "R":
        pos = (pos[0] + 1, pos[1])
    else:
        if T == 1:
            if pos[0] > 0:
                pos = (pos[0] + 1, pos[1])
            else:
                pos = (pos[0] - 1, pos[1])
        else:
            if pos[0] > 0:
                pos = (pos[0] - 1, pos[1])
            elif pos[0] < 0:
                pos = (pos[0] + 1, pos[1])
            else:
                if pos[1] > 0:
                    pos = (pos[0], pos[1] - 1)
                else:
                    pos = (pos[0], pos[1] + 1)

print(abs(pos[0]) + abs(pos[1]))
