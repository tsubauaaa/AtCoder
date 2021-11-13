N, K, A = map(int, input().split())
nums = [i for i in range(1, N+1)]
nums *= K
for i, a in enumerate(nums[A-1:]):
    if i + 1 == K:
        print(a)
        exit()