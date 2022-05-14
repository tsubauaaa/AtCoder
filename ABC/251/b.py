import itertools

N, W = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for i in range(3):
    for nums in itertools.combinations(A, i + 1):
        sum_nums = sum(nums)
        if sum_nums > W:
            continue
        ans.append(sum_nums)
print(len(set(ans)))
