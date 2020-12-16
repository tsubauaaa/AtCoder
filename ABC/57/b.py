N, M = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
points = [list(map(int, input().split())) for _ in range(M)]

ans = [0] * N
for i in range(N):
    min_d = 4 * 10 ** 8 + 1
    for j in range(M):
        d = abs(students[i][0] - points[j][0]) + abs(students[i][1] - points[j][1])
        if min_d > d:
            ans[i] = j + 1
            min_d = d
for ansi in ans:
    print(ansi)
