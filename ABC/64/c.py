N = int(input())
a = list(map(int, input().split()))
rates = [0] * 9

for i in range(N):
    if 1 <= a[i] <= 399:
        rates[0] += 1
    elif 400 <= a[i] <= 799:
        rates[1] += 1
    elif 800 <= a[i] <= 1199:
        rates[2] += 1
    elif 1200 <= a[i] <= 1599:
        rates[3] += 1
    elif 1600 <= a[i] <= 1999:
        rates[4] += 1
    elif 2000 <= a[i] <= 2399:
        rates[5] += 1
    elif 2400 <= a[i] <= 2799:
        rates[6] += 1
    elif 2800 <= a[i] <= 3199:
        rates[7] += 1
    else:
        rates[8] += 1

not_range = 0
over_range = rates[-1]
for rate in rates[:8]:
    if rate == 0:
        not_range += 1
rate_range = 8 - not_range

# print(rate_range=2, not_range=6, over_range=5)

if rate_range == 0:
    print(1, min(over_range, 8))
else:
    # print(
    #     rate_range + max(0, over_range - rate_range),
    #     rate_range + min(over_range, not_range),
    # )
    print(rate_range, rate_range + rates[-1])
