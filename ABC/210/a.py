N,A,X,Y=map(int,input().split())
ans = 0
for i in range(1,N+1):
    if i > A:
        ans += Y
    else:
        ans += X
print(ans)
