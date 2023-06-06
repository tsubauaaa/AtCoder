C = []
for i in range(3):
    C.append(list(map(int, input().split())))

ans = True

if not (((C[0][0] - C[0][1]) == (C[1][0] - C[1][1])) and ((C[1][0] - C[1][1]) == (C[2][0] - C[2][1]))):
    ans = False

if not (((C[0][1] - C[0][2]) == (C[1][1] - C[1][2])) and ((C[1][1] - C[1][2]) == (C[2][1] - C[2][2]))):
    ans = False

if not (((C[0][0] - C[1][0]) == (C[0][1] - C[1][1])) and ((C[0][1] - C[1][1]) == (C[0][2] - C[1][2]))):
    ans = False

if not (((C[1][0] - C[2][0]) == (C[1][1] - C[2][1])) and ((C[1][1] - C[2][1]) == (C[1][2] - C[2][2]))):
    ans = False

if ans:
    print("Yes")
else:
    print("No")
