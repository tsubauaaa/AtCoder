X = int(input())
ans = 100
year = 0
while ans < X:
    interest = ans // 100
    ans += interest
    year += 1
print(year)
