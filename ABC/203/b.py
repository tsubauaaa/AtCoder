N,K=map(int,input().split())

ans = []
for i in range(N):
    for j in range(K):
        ans.append(int(str(i+1)+'0'+str(j+1)))
print(sum(ans))