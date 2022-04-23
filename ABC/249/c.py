import collections
import itertools

N, K = map(int, input().split())
C = []
for i in range(N):
    s = input()
    C.append(collections.Counter(s))

sum_C = []

for i in range(1, N + 1):
    for v in itertools.combinations(C, i):
        sum_v = collections.Counter()
        for vv in v:
            sum_v += vv
        sum_C.append(sum_v)

ans = 0

for sum_c in sum_C:
    ans = max(ans, list(sum_c.values()).count(K))

print(ans)
