N, M, Q = map(int, input().split())
solves, scores = {}, {}
for i in range(N):
    solves[i + 1] = []
    scores[i + 1] = N
ans = []
for q in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 2:
        solves[s[1]].append(s[2])
        scores[s[2]] -= 1
    else:
        tmp = 0
        for solve in solves[s[1]]:
            tmp += scores[solve]
        ans.append(tmp)

for ansi in ans:
    print(ansi)
