from decimal import ROUND_CEILING, Decimal

R, X, Y = map(int, input().split())

ans = Decimal.sqrt(
    Decimal(str(X)) ** Decimal("2") + Decimal(str(Y)) ** Decimal("2")
) / Decimal(str(R))
print(ans.quantize(Decimal("0"), rounding=ROUND_CEILING))
