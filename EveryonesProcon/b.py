g = {i + 1: [] for i in range(4)}
for i in range(3):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
odd_cnt = 0
for k, v in g.items():
    if len(v) % 2 != 0:
        odd_cnt += 1
if odd_cnt in (0, 2):
    print("YES")
else:
    print("NO")
