N = int(input())
ans = 0
for i in range(N):
    diff = list(map(int, input().split()))
    S = 0
    for j in range(5):
        S += diff[j]
    if 0 <= S < 20:
        ans += 1
print(ans)
