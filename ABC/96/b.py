nums = list(map(int, input().split()))
K = int(input())

for i in range(K):
    nums.sort(reverse=True)
    nums[0] = nums[0] * 2
print(sum(nums))
