N,P=map(int,input().split())
a = list(map(int,input().split()))

ans = 0
for ai in a:
    if ai < P:
        ans += 1

print(ans)