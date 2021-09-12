A,B,T=map(int,input().split())
ans = 0
i = 1
while A*i <= T+0.5:
    ans += B
    i += 1
    A*i
print(ans)