import math


def sigma(frm, to):
    result = 0
    for i in range(frm, to + 1):
        for j in range(frm, to + 1):
            tmp = math.gcd(i, j)
            for k in range(frm, to + 1):
                result += math.gcd(tmp, k)
    return result


K = int(input())

print(sigma(1, K))
