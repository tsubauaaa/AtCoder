A, B, C, D = map(int, input().split())
blue = A
red = 0
for i in range(10**6):
    if blue <= red * D:
        break
    blue += B
    red += C
else:
    i = -1
print(i)
