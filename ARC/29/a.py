from itertools import combinations


def split(lst, index):
    d = {}
    for c in combinations(lst, index):
        t1 = tuple(sorted(c))
        t2 = tuple(sorted(set(lst) - set(c)))

        k, v = (t1, t2) if t1 < t2 else (t2, t1)
        d[k] = v
    return d


N = int(input())
t = [int(input()) for _ in range(N)]
lst = [i for i in range(N)]
ans = 0
if N == 1:
    ans = t[0]
elif N == 2:
    ans = max(t)
else:
    for i in range(1, N - 1):
        pairs = split(lst, i)
        max_nums = []
        for g1, g2 in pairs.items():
            sum_g1 = 0
            for g in g1:
                sum_g1 += t[g]
            sum_g2 = 0
            for g in g2:
                sum_g2 += t[g]
            if len(g1) == 3 and sum_g2 > sum_g1:
                ans = sum_g2
                print(ans)
                exit()
            if len(g2) == 3 and sum_g1 > sum_g2:
                ans = sum_g1
                print(ans)
                exit()
            max_nums.append(max(sum_g1, sum_g2))
    ans = min(max_nums)
print(ans)
