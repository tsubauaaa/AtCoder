import itertools

N, K = map(int, input().split())
T1 = list(map(int, input().split()))
T = []
nums = []
for i in range(1, N):
    T.append(list(map(int, input().split())))
    nums.append(i + 1)
perms = list(itertools.permutations(nums, N - 1))
ans = 0
# 順列ごとループ
for i in range(len(perms)):
    # 最初に1->?の時間で初期化
    times = T1[perms[i][0] - 1]
    # 順列の中身をループ
    for j in range(len(nums)):
        if j != len(nums) - 1:
            times += T[perms[i][j] - 2][perms[i][j + 1] - 1]
        else:
            times += T[perms[i][j] - 2][0]
    if times == K:
        ans += 1
print(ans)
