N = int(input())
masu = []
ans = []
for _ in range(N):
    s = input()
    ss = []
    for i in range(2*N-1):
        ss.append(s[i])
    masu.append(ss)
    ans.append(ss)

for i in range(N-2, -1, -1):
    for j in range(2 * N - 1):
        if 1 <= j <= 2 * N - 3:
            if masu[i][j] != "#":
                continue
            if masu[i+1][j-1] == "X" or masu[i+1][j] == "X" or masu[i+1][j+1] == "X":
                ans[i][j] = "X"

for ai in ans:
    print(''.join(ai))
