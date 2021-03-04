S = input()
w = int(input())
ans = []
tmp = []
j = 1
for i in range(len(S)):
    tmp.append(S[i])
    if i == j * w - 1:
        ans.append(tmp)
        tmp = []
        j += 1
    if i == len(S) - 1 and len(tmp) != 0:
        ans.append(tmp)

for ansi in ans:
    print(ansi[0], end="")
