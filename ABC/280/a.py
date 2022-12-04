H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for s in S:
    for si in s:
        if si == "#":
            ans += 1

print(ans)