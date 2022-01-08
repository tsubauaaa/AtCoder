import itertools
import math

N = int(input())
axis = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for pair in itertools.combinations(axis, 2):
    d = math.sqrt((pair[0][0] - pair[1][0]) ** 2 + (pair[0][1] - pair[1][1]) ** 2)
    ans = max(ans, d)

print(ans)
