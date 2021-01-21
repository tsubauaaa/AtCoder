A, B, C = map(int, input().split())
for X in range(1, 10001):
    if X % B == C:
        if X % A == 0:
            print("YES")
            exit()
print("NO")
