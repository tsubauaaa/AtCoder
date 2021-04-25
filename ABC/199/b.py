N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_max = max(A)
B_max = max(B)
max_AB = max(A_max, B_max)
nums = [i for i in range(1, max_AB + 1)]

i = 1
ans = []
for a, b in zip(A, B):
    for i in range(max_AB):
        if a <= nums[i] <= b:
            continue
        else:
            nums[i] = -1

print(max_AB - nums.count(-1))
