X, Y, Z = map(int, input().split())

is_wall = False
is_break = True
if 0 <= Y <= X:
    is_wall = True
    if Y < Z:
        is_break = False
elif X <= Y <= 0:
    is_wall = True
    if Z < Y:
        is_break = False

if not is_break:
    print(-1)
    exit()

ans = 0
if is_wall:
    ans = abs(0 - Z) + abs(X - Z)
else:
    ans = abs(X - 0)

print(ans)
