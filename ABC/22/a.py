N, S, T = map(int, input().split())
weights = [int(input()) for _ in range(N)]
cs = [sum(weights[: i + 1]) for i in range(N)]
ans = 0
for w in cs:
    if S <= w <= T:
        ans += 1
print(ans)
