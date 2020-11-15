N, M = map(int, input().split())
nums = [-1] * N
for i in range(M):
    s, c = map(int, input().split())
    if nums[s - 1] == -1:
        nums[s - 1] = c
        continue
    if nums[s - 1] == 0:
        nums[s - 1] = c
    else:
        if nums[s - 1] != c:
            print(-1)
            exit()
min_num = 0
max_num = 0
if N == 1:
    min_num = 0
    max_num = 9
elif N == 2:
    min_num = 10
    max_num = 99
elif N == 3:
    min_num = 100
    max_num = 999

match_cnt = N - nums.count(-1)
nums = list(map(str, nums))
for i in range(min_num, max_num + 1):
    string_i = str(i)
    cnt = 0
    for j, num in zip(string_i, nums):
        if num == "-1":
            continue
        if j == num:
            cnt += 1
    if cnt == match_cnt:
        print(string_i)
        exit()

print(-1)
