from collections import deque

N, X, Y = map(int, input().split())
dist = {}
obstacle = {}
for i in range(-201, 202):
    for j in range(-201, 202):
        dist[(i, j)] = -1
        obstacle[(i, j)] = True
for _ in range(N):
    x, y = list(map(int, input().split()))
    obstacle[(x, y)] = False

Q = deque()
Q.append([0, 0])
dist[(0, 0)] = 0

while len(Q) > 0:
    i, j = Q.popleft()
    for i2, j2 in [[i + 1, j + 1], [i, j + 1], [i - 1, j + 1], [i + 1, j], [i - 1, j], [i, j - 1]]:
        if not (-201 <= i2 <= 201 and -201 <= j2 <= 201):
            continue
        if not obstacle[(i, j)]:
            continue
        if not dist[(i2, j2)] == -1:
            continue
        dist[(i2, j2)] = dist[(i, j)] + 1
        Q.append([i2, j2])
print(dist[(X, Y)])
