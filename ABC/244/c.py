N = int(input())

check = [True] * 2 * (N + 1)
while True:
    for i in range(2 * (N + 1)):
        if check[i]:
            check[i] = False
            print(i + 1)
            break
    A = int(input())
    if A == 0:
        break
    check[A - 1] = False
