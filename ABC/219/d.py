N = int(input())
X,Y=map(int,input().split())
bentos = []
for _ in range(N):
    bentos.append(list(map(int,input().split())))

ans = []
for i in range(2**N):
    takoyaki = 0
    taiyaki = 0
    cnt = 0
    for j in range(N):
        if (i >> j) & 1:
            cnt += 1
            takoyaki += bentos[j][0]
            taiyaki += bentos[j][1]
    if takoyaki >= X and taiyaki >= Y:
        ans.append(cnt)

print(-1 if not ans else min(ans))
