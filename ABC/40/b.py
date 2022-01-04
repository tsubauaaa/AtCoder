n = int(input())
ans = 10 ** 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j > n:
            break
        ans = min(ans, abs(i - j) + n - i * j)

print(ans)
