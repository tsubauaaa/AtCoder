import copy

A = [list(map(int, input().split())) for _ in range(4)]
r_A = copy.deepcopy(A)
for h in range(4):
    for w in range(2, -1, -1):
        if r_A[h][w + 1] != 0:
            if A[h][w] == A[h][w + 1]:
                r_A[h][w] = 0
                r_A[h][w + 1] = 2 * A[h][w]
        else:
            r_A[h][w + 1] = r_A[h][w]
            r_A[h][w] = 0
l_A = copy.deepcopy(A)
for h in range(4):
    for w in range(1, 4):
        if l_A[h][w - 1] != 0:
            if A[h][w] == A[h][w - 1]:
                l_A[h][w] = 0
                l_A[h][w - 1] = 2 * A[h][w]
        else:
            l_A[h][w - 1] = l_A[h][w]
            l_A[h][w] = 0
u_A = copy.deepcopy(A)
for w in range(4):
    for h in range(2, -1, -1):
        if u_A[h + 1][w] != 0:
            if A[h][w] == A[h + 1][w]:
                u_A[h][w] = 0
                u_A[h + 1][w] = 2 * A[h][w]
        else:
            u_A[h + 1][w] = u_A[h][w]
            u_A[h][w] = 0
d_A = copy.deepcopy(A)
for w in range(4):
    for h in range(1, 4):
        if d_A[h - 1][w] != 0:
            if A[h][w] == A[h - 1][w]:
                d_A[h][w] = 0
                d_A[h - 1][w] = 2 * A[h][w]
        else:
            d_A[h - 1][w] = d_A[h][w]
            d_A[h][w] = 0
for a in [r_A, l_A, u_A, d_A]:
    if a != A:
        print("CONTINUE")
        exit()
print("GAMEOVER")
