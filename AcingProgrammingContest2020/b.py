N = int(input())
a = list(map(int, input().split()))

nums = {i+1: ai for i, ai in enumerate(a)}
ans = 0
for k, v in nums.items():
    if k % 2 != 0 and v % 2 != 0:
        ans += 1

print(ans)
