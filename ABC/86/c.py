N = int(input())
before_x, before_y, before_t = 0, 0, 0
ans = True
for i in range(N):
    t, x, y = map(int, input().split())
    dis = abs(x - before_x) + abs(y - before_y)
    T = t - before_t
    if T - dis < 0:
        ans = False
    else:
        if (T - dis) % 2 == 0:
            before_x, before_y, before_t = x, y, t
        else:
            ans = False
print("Yes" if ans else "No")
