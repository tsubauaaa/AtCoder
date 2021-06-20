N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1, 2):
    ans += 1
print("YES" if ans >= K else "NO")
