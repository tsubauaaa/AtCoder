L, R = map(int, input().split())
ans = 2 * 10 ** 9
for i in range(L % 2019, R % 2019):
    for j in range((L + 1) % 2019, (R + 1) % 2019):
        ans = min(ans, i * j % 2019)

print(ans % 2019)
