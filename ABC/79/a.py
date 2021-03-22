from itertools import groupby

N = input()
ans = "No"
for c, g in groupby(N):
    if len(list(g)) >= 3:
        ans = "Yes"
print(ans)
