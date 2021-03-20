a, b = map(int, input().split())
c, d = map(int, input().split())

ans = -201
for x in range(a, b + 1):
    for y in range(c, d + 1):
        tmp = x - y
        ans = max(ans, tmp)
print(ans)
