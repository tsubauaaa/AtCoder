A = int(input())
lim = int(1000000 ** (1 / 3)) + 2
for i in range(lim):
    if i ** 3 == A:
        print("YES")
        exit()
print("NO")
