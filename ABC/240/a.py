a, b = map(int, input().split())

if a == 1:
    if b == 10 or b == 2:
        print("Yes")
        exit()
else:
    if b == a - 1 or b == a + 1:
        print("Yes")
        exit()
print("No")

