N, X = map(int, input().split())
donuts = [int(input()) for _ in range(N)]
X -= sum(donuts)
print(N + X // min(donuts))
