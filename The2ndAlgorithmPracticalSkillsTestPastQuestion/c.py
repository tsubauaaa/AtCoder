N = int(input())
masu = []
ans = []
for i in range(N):
    S = input()
    row = []
    for j in range(2*N-1):
        row.append(S[j])
    masu.append(row)
    ans.append(masu[i])

print(masu)

for i in range(N-1, -1, -1):
    for j in range(2, 2*N-1):
        if masu[i][j] == "#":
            print(i, j)
            if i+1 > N - 1:
                continue
            if masu[i+1][j-1] == "X" or masu[i+1][j] == "X" or masu[i+1][j+1] == "X":
                ans[i][j] = "X"

for ansi in ans:
    print("".join(ansi))
