X, Y = map(int, input().split())
A = min(X, Y)
B = max(X, Y)
if A + 3 > B:
    print("Yes")
else:
    print("No")
