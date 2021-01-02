from itertools import combinations

nums = list(map(int, input().split()))
combs = combinations(nums, 3)

ans = map(lambda x: sum(x), combs)
ans = list(ans)
ans.sort()
print(ans[-3])
