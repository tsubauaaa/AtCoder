ans = [0] * 3
for i in range(3):
    s, e = map(int, input().split())
    ans[i] = s * e / 10
print(int(sum(ans)))
