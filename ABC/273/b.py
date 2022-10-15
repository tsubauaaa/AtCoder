from decimal import ROUND_HALF_UP, Decimal

X, K = map(int, input().split())

for i in range(K):
    kurai = "1E" + str(i + 1)
    X = int(Decimal(X).quantize(Decimal(kurai), rounding=ROUND_HALF_UP))

print(X)
