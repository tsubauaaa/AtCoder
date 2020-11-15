N = int(input())
ans = 0
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        ans += i
    else:
        if i % 3 == 0:
            ans += i
        elif i % 5 == 0:
            ans += i
print((N * (N + 1) // 2) - ans)
