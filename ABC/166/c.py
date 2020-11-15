N, M = map(int, input().split())
H = list(map(int, input().split()))
height = [[H[i]] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    height[a - 1].append(H[b - 1])
    height[b - 1].append(H[a - 1])
ans = 0
for i in range(N):
    if len(height[i][1:]) != 0:
        max_height = max(height[i][1:])
    else:
        max_height = 0
    if height[i][0] > max_height:
        ans += 1
print(ans)
