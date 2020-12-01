n = int(input())
ans = 0
for i in range(2, n):
    for j in range(2, n + 1):
        if i % j == 0:
            break
    if i == j:
        ans += 1
print(ans)
