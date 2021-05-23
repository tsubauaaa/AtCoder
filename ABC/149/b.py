A,B,K=map(int,input().split())

if K -A >= 0:
    B = max(0, B-(K-A))
    A = 0
else:
    A -= K 
print(A,B)