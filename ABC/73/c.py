from collections import Counter

N = int(input())
nums = [int(input()) for _ in range(N)]
c = Counter(nums)
ans = 0
for k, v in c.items():
    if v % 2 != 0:
        ans += v % 2
print(ans)
