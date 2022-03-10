A, B, C = map(int, input().split())
nums = {"A": A, "B": B, "C": C}
sorted_nums = sorted(nums.items(), key=lambda x: x[1])

for i, n in enumerate(sorted_nums):
    if i == 1:
        print(n[0])
        exit()
