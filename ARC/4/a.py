import math
from itertools import combinations


def calc_line(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)


N = int(input())
coordinates = []
ans = 0
for i in range(N):
    x, y = map(int, input().split())
    coordinates.append([x, y])
for c in combinations(coordinates, 2):
    line = calc_line(c[0], c[1])
    ans = max(ans, line)
print(ans)
