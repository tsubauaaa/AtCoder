N = int(input())
H = list(map(int, input().split()))
ans = 1
high = H[0]
for i in range(1, N):
    if high <= H[i]:
        ans += 1
        high = H[i]
print(ans)
