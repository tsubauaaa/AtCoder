R, G, B, N = map(int, input().split())
ans = 0
for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if R * i + G * j + B * k == N:
                ans += 1
print(ans)
