N = int(input())
ans = [0] * 1001
ans[1] = 1
for i in range(1, 1000):
    ans[i + 1] = ans[i] + i + 1
print(ans[N])
