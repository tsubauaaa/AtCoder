from itertools import combinations

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
for i in range(1, N + 1):
    for c in combinations(A, i):
        print(c, c[0] * c[-1])
        ans += c[0] * c[-1]
print(ans % 998244353)
