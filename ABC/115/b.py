N = int(input())
prices = [int(input()) for _ in range(N)]
prices.sort(reverse=True)

ans = 0
for price in prices[1:]:
    ans += price
print(ans + prices[0] // 2)
