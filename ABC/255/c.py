import math

X, A, D, N = map(int, input().split())

# nums = [A + i * D for i in range(N)]

# print(nums)

if D == 0:
    print(abs(X - A))
    exit()

n = (X - A) / D

n1 = math.floor(n)
n2 = n1 + 1
ans1 = 0
ans2 = 0

if 0 <= n1 <= N - 1:
    ans1 = abs(X - (A + n1 * D))
else:
    ans1 = min(abs(X - (A + (N - 1) * D)), abs(X - (A + 0 * D)))

if 0 <= n2 <= N - 1:
    ans2 = abs(X - (A + n2 * D))
else:
    ans2 = min(abs(X - (A + (N - 1) * D)), abs(X - (A + 0 * D)))

print(min(ans1, ans2))
