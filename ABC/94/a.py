A, B, X = map(int, input().split())

if A > X:
    print("NO")
    exit()

if A+B < X:
    print("NO")
    exit()

print("YES")
