L1, R1, L2, R2 = map(int, input().split())

nums = [[i, 0] for i in range(101)]

for i in range(L1, R1):
    nums[i][1] += 1

for i in range(L2, R2):
    nums[i][1] += 1
ans = 0
for num in nums:
    if num[1] == 2:
        ans += 1

print(ans)

