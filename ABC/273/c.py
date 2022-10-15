import bisect
import copy

N = int(input())
A = list(map(int, input().split()))
B = copy.deepcopy(list(set(A)))
B.sort()
len_B = len(B)

ans = {i: 0 for i in range(N)}

for a in A:
    # k = len_B - (B.index(a) + 1)
    # print(a, bisect.bisect_right(B, a))
    k = len_B - bisect.bisect_right(B, a)
    ans[k] += 1

for k, v in ans.items():
    print(v)
