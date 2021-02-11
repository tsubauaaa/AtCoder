import math

N, X = map(int, input().split())
xs = list(map(int, input().split()))
xs.append(X)
xs.sort()
diffs = []
for i in range(1, N + 1):
    diffs.append(xs[i] - xs[i - 1])
if len(diffs) == 1:
    print(diffs[0])
elif len(diffs) == 2:
    print(math.gcd(diffs[0], diffs[1]))
else:
    ans = math.gcd(diffs[0], diffs[1])
    for i in range(2, N):
        ans = math.gcd(ans, diffs[i])
    print(ans)
