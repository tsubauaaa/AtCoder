N, D, H = map(int, input().split())


def simultaneous_equations(d, h):
    # a = (h - H) / (d - D)
    b = (d * H - D * h) / (d - D)
    return b


ans = 0.0
for i in range(N):
    d, h = map(int, input().split())
    tmp = simultaneous_equations(d, h)
    ans = max(tmp, ans)

print(float(ans))
