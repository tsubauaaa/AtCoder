from itertools import combinations

N = int(input())
coordinate = []
for i in range(N):
    x, y = map(int, input().split())
    coordinate.append((x, y))
ans = 0
for v in combinations(coordinate, 2):
    tilt = (v[1][1] - v[0][1]) / (v[1][0] - v[0][0])
    if -1 <= tilt <= 1:
        ans += 1
print(ans)
