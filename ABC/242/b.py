S = input()
d = {}
for s in S:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

sorted_d = sorted(d.items())

ans = ""

for k, v in sorted_d:
    ans += k * v

print(ans)
