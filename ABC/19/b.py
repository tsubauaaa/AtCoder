from itertools import groupby

s = input()
ans = ""
for c, g in groupby(s):
    ans += c + str(len(list(g)))
print(ans)
