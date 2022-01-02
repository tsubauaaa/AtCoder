N = int(input())
S = input()
accessories = "b"

if accessories == S:
    print(0)
    exit()

j = 1
for i in range(100):
    if j == 1:
        accessories = "a" + accessories + "c"
    elif j == 2:
        accessories = "c" + accessories + "a"
    else:
        accessories = "b" + accessories + "b"
    if j != 2:
        j += 1
    else:
        j = 0
    if accessories == S:
        print(i + 1)
        exit()
print(-1)
