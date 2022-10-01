N, Q = map(int, input().split())

nums = []

for _ in range(N):
    ns = list(map(int, input().split()))
    nums.append(ns[1:])

for i in range(Q):
    s, t = map(int, input().split())
    print(nums[s - 1][t - 1])
