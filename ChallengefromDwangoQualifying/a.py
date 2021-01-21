N = int(input())
a = list(map(int, input().split()))
avg = sum(a) / N
ans = [0] * N
for i in range(N):
    ans[i] = abs(a[i] - avg)
print(ans.index(min(ans)))
