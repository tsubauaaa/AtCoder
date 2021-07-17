import copy
from collections import Counter

N, K = map(int, input().split())
c = list(map(int, input().split()))

counts_dic = {ci: 0 for ci in c}
counts_list = [{} for _ in range(N)]
for i in range(N):
    counts_dic[c[i]] += 1
    counts_list[i] = copy.deepcopy(counts_dic)

ans = 0
for i in range(N):
    if i % (K - 1) == 0:
        ans = max(
            ans, len(Counter(counts_list[i]) - Counter(counts_list[i - K])))
        # print(Counter(counts_list[i]) - Counter(counts_list[i - K]))
print(ans)
