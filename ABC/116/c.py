def split_h(h):
    hs = []
    for hi in h:
        if hi not in (0, 1):
            hs.append(hi - 1)
    return hs


N = int(input())
h = list(map(int, input().split()))
ans = 0
while sum(h) != 0:
    print(h)
    h = split_h(h)
    ans += 1
print(ans)
