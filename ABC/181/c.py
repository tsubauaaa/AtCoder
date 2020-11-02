from itertools import combinations


def collinear(p0, p1, p2):
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
    return abs(x1 * y2 - x2 * y1) < 1e-12


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
base = list(combinations(points, 3))
ans = "No"
for b in base:
    if collinear(b[0], b[1], b[2]):
        ans = "Yes"

print(ans)
