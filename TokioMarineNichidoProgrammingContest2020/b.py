A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if V == W:
    print("NO")
    exit()
if A < B:
    x = (B - A) / (V - W)
else:
    x = (B - A) / (W - V)
if 1 <= x <= T:
    print("YES")
else:
    print("NO")
