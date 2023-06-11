N = int(input())

cnt = 0
for i in range(1, 555556, 1):
    si = str(i)
    ok = True
    for s in si:
        if s != si[0]:
            ok = False
    if ok:
        cnt += 1
    if cnt == N:
        print(i)
        exit()
