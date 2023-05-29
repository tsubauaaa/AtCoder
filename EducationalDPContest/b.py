N, K = map(int, input().split())
h = list(map(int, input().split()))

costs = [0] * N
costs[0] = 0
costs[1] = costs[0] + abs(h[0] - h[1])

for i in range(2, N):
    costs[i] = costs[i-1] + abs(h[i-1] - h[i])
    for j in range(2, K+1):
        if i - j < 0:
            continue
        cost = abs(h[i - j] - h[i])
        costs[i] = min(costs[i - j] + cost, costs[i])

print(costs[N-1])
