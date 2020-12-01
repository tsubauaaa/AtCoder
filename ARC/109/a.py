a, b, x, y = map(int, input().split())
if a == b:
    print(x)
    exit()
if a < b:
    # 登り
    print(min((b - a) * 2 * x + x, (b - a) * y + x))
    # print(f"x only: {(b - a) * 2 * x + x}")
    # print(f"1x+y: {(b - a) * y + x}")
else:
    # 降り
    if a - b == 1:
        print(min(x, (a - b) * y + x))
        # print(f"x only: {x}")
        # print(f"1x+y: {(a - b) * y + x}")
    else:
        print(min((a - (b + 1)) * 2 * x + x, (a - (b + 1)) * y + x))
        # print(f"x only: {(a - (b + 1)) * 2 * x + x}")
        # print(f"1x+y: {(a - (b + 1)) * y + x}")
