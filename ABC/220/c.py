N=int(input())
A=list(map(int,input().split()))
X=int(input())
sum_A = sum(A)
p = X//sum_A

sum_B = sum_A * p
for q in range(N):
    sum_B += A[q]
    if sum_B > X:
        print(p*N+q+1)
        exit()
