A,B,K=map(int,input().split())

ans = []
for i in range(2**(A+B)):
    p = ""
    for j in range(A+B):
        if i >> j & 1:
            p += "a"
        else:
            p += "b"
    ans.append(p)
print(ans)