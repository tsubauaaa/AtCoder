from itertools import combinations
N = int(input())
d = list(map(int, input().split()))

ans = 0
for c in combinations(d, 2):
    ans += c[0]*c[1]
print(ans)