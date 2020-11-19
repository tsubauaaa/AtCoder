N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    score = i
    x = 0
    while score <= K - 1:
        score *= 2
        x += 1
    ans += 1 / N * (1 / 2) ** x
print(ans)
