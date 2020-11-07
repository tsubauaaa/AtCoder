nums = list(map(int, input().split()))
ans = 0
while True:
    if nums[0] == nums[1] == nums[2]:
        break
    ma = max(nums)
    ma_cnt = nums.count(ma)
    for i in range(len(nums)):
        if nums[i] != ma:
            if ma_cnt == 1:
                nums[i] += 1
            elif ma_cnt == 2:
                nums[i] += 2
    ans += 1

print(ans)
