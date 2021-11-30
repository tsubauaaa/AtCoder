A, B = input().split()

A_N = len(A)
B_N = len(B)

for i in range(min(A_N, B_N)):
    a = A[A_N-i-1]
    b = B[B_N-i-1]
    if int(a)+int(b) > 9:
        print("Hard")
        exit()

print("Easy")
