N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
cnt = 0
ans = 0
for i in range(N):
    cnt += s.count(s[i])
    cnt -= t.count(s[i])
    ans = max(ans, cnt)
    cnt = 0
print(ans)
