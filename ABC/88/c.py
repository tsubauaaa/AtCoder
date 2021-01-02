C = [list(map(int, input().split())) for _ in range(3)]
for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1 = C[0][0] - a1
            b2 = C[0][1] - a1
            b3 = C[0][2] - a1
            A = [a1, a2, a3]
            B = [b1, b2, b3]
            ok = True
            for i in range(3):
                for j in range(3):
                    if C[i][j] != A[i] + B[j]:
                        ok = False
            if ok:
                print("Yes")
                exit()
print("No")
