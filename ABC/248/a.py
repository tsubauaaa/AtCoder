S = input()
nums = [False] * 10


for s in S:
    nums[int(s)] = True

for i in range(10):
    if not nums[i]:
        print(i)
        break
