A, B = map(int, input().split())
if A * 6 < B:
    print("No")
    exit()

if B < A:
    print("No")
    exit()

print("Yes")
