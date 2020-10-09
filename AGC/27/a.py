N, x = map(int, input().split())
aaa = list(map(int, input().split()))
aaa.sort()
ans = 0

for a in aaa:
    if x < a:
        break
    ans += 1
    x -= a
else: 
    if x > 0:
        ans -= 1

print(ans)