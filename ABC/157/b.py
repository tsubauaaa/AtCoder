card = []
bingo = []
for i in range(3):
    card.append(list(map(int, input().split())))
    bingo.append([False]*3)

N = int(input())

for i in range(N):
    num = int(input())
    for j in range(3):
        for k in range(3):
            if card[j][k] == num:
                bingo[j][k] = True

ans = False

if (bingo[0][0] and bingo[0][1] and bingo[0][2]):
    ans = True

if (bingo[1][0] and bingo[1][1] and bingo[1][2]):
    ans = True

if (bingo[2][0] and bingo[2][1] and bingo[2][2]):
    ans = True

if (bingo[0][0] and bingo[1][0] and bingo[2][0]):
    ans = True

if (bingo[0][1] and bingo[1][1] and bingo[2][1]):
    ans = True

if (bingo[0][2] and bingo[1][2] and bingo[2][2]):
    ans = True

if (bingo[0][0] and bingo[1][1] and bingo[2][2]):
    ans = True

if (bingo[0][2] and bingo[1][1] and bingo[2][0]):
    ans = True

if ans:
    print("Yes")
else:
    print("No")
