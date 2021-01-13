N = int(input())
a = list(map(int, input().split()))
ans = [0] * (10 ** 5 + 2)

for ai in a:
    ans[ai] += 1
    ans[ai + 1] += 1
    ans[ai - 1] += 1
print(max(ans))
