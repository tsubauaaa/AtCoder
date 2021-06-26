import itertools
N = int(input())
sections = []
for i in range(N):
    t, l, r = map(int, input().split())
    if t == 1:
        sections.append([l, r])
    elif t == 2:
        sections.append([l, r - 0.1])
    elif t == 3:
        sections.append([l + 0.1, r])
    else:
        sections.append([l + 0.1, r - 0.1])
combs = itertools.combinations(sections, 2)

ans = 0
for c in combs:
    if c[0][0] <= c[1][0]:
        if c[0][1] >= c[1][0]:
            ans += 1
    elif c[0][0] >= c[1][0]:
        if c[1][1] >= c[0][0]:
            ans += 1

print(ans)
