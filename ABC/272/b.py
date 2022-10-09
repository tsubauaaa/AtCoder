N, M = map(int, input().split())
check = {}

for i in range(N):
    for j in range(i + 1, N):
        check[str(i + 1) + "," + str(j + 1)] = False

for i in range(M):
    kx = list(map(int, input().split()))
    k = kx[0]
    member = [False] * N
    for k in kx[1:]:
        member[k - 1] = True

    for k, v in check.items():
        if v:
            continue
        k1, k2 = k.split(",")
        k1, k2 = int(k1), int(k2)
        if member[k1 - 1] and member[k2 - 1]:
            check[k] = True

for k, v in check.items():
    if not v:
        print("No")
        exit()
print("Yes")
