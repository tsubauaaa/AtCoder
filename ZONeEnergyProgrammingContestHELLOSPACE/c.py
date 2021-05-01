N = int(input())
A_max = 0
B_max = 0
C_max = 0
D_max = 0
E_max = 0
for i in range(N):
    A, B, C, D, E = map(int, input().split())
    print(A + B + C + D + E)
    A_max = max(A, A_max)
    B_max = max(B, B_max)
    C_max = max(C, C_max)
    D_max = max(D, D_max)
    E_max = max(E, E_max)

# print(min(A_max, B_max, C_max, D_max, E_max))
