from itertools import groupby

S = input()
K = int(input())
runlength = []
for c, g in groupby(S):
    runlength.append(len(list(g)))
cnt = 0
for rl in runlength:
    if rl >= 2:
        cnt += rl // 2

if len(runlength) == 1:
    print(runlength[0] * K // 2)
    exit()

if S[0] == S[-1] and runlength[0] % 2 != 0 and runlength[-1] % 2 != 0:
    cnt += 1
    print(cnt * K - 1)
else:
    print(cnt * K)
