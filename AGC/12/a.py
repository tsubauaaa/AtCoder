N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
for i in range(N):
    ans += a[(i + 1) * 2 - 1]
print(ans)
