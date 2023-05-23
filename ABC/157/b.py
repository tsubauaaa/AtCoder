bingo = []
for i in range(3):
    bingo.append(list(map(int, input().split())))
N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
paper = []
for i in range(N):
    for j in range(3):
        for k in range(3):
            if bingo[j][k] == nums[i]:
                paper.append([j+1, k+1])
ans = 0
hits = [[[1, 1], [2, 1], [3, 1]],
        [[1, 2], [2, 2], [3, 2]],
        [[1, 3], [2, 3], [3, 3]],
        [[1, 1], [1, 2], [1, 3]],
        [[2, 1], [2, 2], [2, 3]],
        [[3, 1], [3, 2], [3, 3]],
        [[1, 1], [2, 2], [3, 3]],
        [[1, 3], [2, 2], [3, 1]]
        ]

for h in hits:
    ans = 0
    for p in paper:
        if p in h:
            ans += 1
    if ans == 3:
        print("Yes")
        exit()
print("No")
