def cumsum(xs):
    result = [xs[0] + 1]
    for x in xs[1:]:
        result.append(result[-1] + 1 + x)
    return result


N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(a)
res = cumsum(a)
print(res)
