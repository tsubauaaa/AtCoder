nums = list(map(int, input().split()))

nums_set = set(nums)

for ns in nums_set:
    if nums.count(ns) == 1:
        print(ns)
        exit()

