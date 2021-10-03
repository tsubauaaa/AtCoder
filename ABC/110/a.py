nums=input().split()

print(
    max(int(nums[0])+int(nums[1]+nums[2]), int(nums[0]+nums[1])+int(nums[2]), int(nums[1])+int(nums[2]+nums[0])))
