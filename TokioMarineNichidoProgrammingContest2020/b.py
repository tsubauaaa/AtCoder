A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V == W:
    if A == B:
        print("YES")
        exit()
    else:
        print("NO")
        exit()

if A < B:
    X = (B - A) // (V - W)
else:
    X = (A - B) // (V - W)
if X > T or X < 1:
    print("NO")
    exit()
if A < B:
    if A + X * V == B + X * W:
        print("YES")
    else:
        print("NO")
else:
    if A - X * V == B - X * W:
        print("YES")
    else:
        print("NO")
