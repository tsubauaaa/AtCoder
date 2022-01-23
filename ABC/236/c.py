N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

s = {s: i for i, s in enumerate(S)}
t = []
for Ti in T:
    t.append(s[Ti])


ans = [False] * N

for ti in t:
    ans[ti] = True

for ansi in ans:
    if ansi:
        print("Yes")
    else:
        print("No")
