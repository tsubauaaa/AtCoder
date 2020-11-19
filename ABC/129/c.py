N, M = map(int, input().split())
is_safe = [True] * (N + 2)
for _ in range(M):
    is_safe[int(input()) + 1] = False
dp = [0] * (N + 2)
dp[1] = 1
# 2段目からループ開始
for i in range(2, N + 2):
    print(i)
    if is_safe[i]:
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 10 ** 9 + 7
    else:
        continue

print(dp[-1] % (10 ** 9 + 7))
