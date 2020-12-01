import math


def calc_days(y, m, d):
    res = (
        365 * y
        + math.floor(y / 4)
        - math.floor(y / 100)
        + math.floor(y / 400)
        + math.floor(306 * (m + 1) / 10)
        + d
        - 429
    )
    return res


y = int(input())
m = int(input())
d = int(input())
if m == 1:
    y -= 1
    m = 13
elif m == 2:
    y -= 1
    m = 14
print(calc_days(2014, 5, 17) - calc_days(y, m, d))
