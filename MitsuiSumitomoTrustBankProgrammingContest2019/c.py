X = int(input())
cnt = X // 100
max_price = 105 * cnt
min_price = 100 * cnt

if min_price <= X <= max_price:
    print(1)
else:
    print(0)
