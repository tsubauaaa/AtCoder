N,K=map(int,input().split())
S=input()

ans = ""

for i in range(N):
    if i == K-1:
        ans += S[i].lower()
        continue
    ans += S[i]
print(ans)