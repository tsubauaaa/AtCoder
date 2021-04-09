from itertools import groupby

N = int(input())
a = list(map(int, input().split()))
ans = 0
for c, g in groupby(a):
    len_g = len(list(g))
    if len_g == 1:
        continue
    else:
        ans += len_g // 2
print(ans)
