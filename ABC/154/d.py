def cumsum(xs):
    result = [(xs[0] + 1) / 2]
    for x in xs[1:]:
        result.append(result[-1] + (x + 1) / 2)
    return result


N, K = map(int, input().split())
P = list(map(int, input().split()))
ans = 0
cs_P = cumsum(P)
for i in range(N - K):
    ans = max(ans, cs_P[i + K] - cs_P[i])
print(ans)
