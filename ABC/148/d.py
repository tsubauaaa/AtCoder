N = int(input())
a = list(map(int, input().split()))
ans = 0
num = 1
for i in range(N):
    if a[i] == num:
        num += 1
        continue
    ans += 1
print(ans if ans != N else -1)
