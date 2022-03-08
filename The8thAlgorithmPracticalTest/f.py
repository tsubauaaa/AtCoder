N = int(input())
S = input()

all = []
zeros = []
for i in range(N):
    all.append(i + 1)
    if S[i] == "0":
        zeros.append(i + 1)
ans = []
j = 0
for i in range(N):
    if S[i] == "1":
        ans.append(all[i])
    else:
        ans.append(zeros[j - 1])
        j += 1

    if S[i] == "0" and ans[i] == i + 1:
        print(-1)
        exit()

print(*ans)
