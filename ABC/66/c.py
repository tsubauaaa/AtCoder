n = int(input())
a = list(map(int, input().split()))
b1 = []
b2 = []
for i in range(n):
    if i % 2 == 0:
        b1.append(a[i])
    else:
        b2.append(a[i])
b2.reverse()
b2.extend(b1)
if len(b2) % 2 == 0:
    print(*b2)
else:
    b2.reverse()
    print(*b2)
