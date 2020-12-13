N, A, B = map(int, input().split())
pebbel = N
for i in range(N):
    if i % 2 == 0:
        pebbel -= A
        if pebbel <= 0:
            print("Ant")
            exit()
    else:
        pebbel -= B
        if pebbel <= 0:
            print("Bug")
            exit()
