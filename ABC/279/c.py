H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

S_row = list(zip(*S))
T_row = list(zip(*T))

S_row.sort()
T_row.sort()

if S_row == T_row:
    print("Yes")
else:
    print("No")