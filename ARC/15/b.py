N = int(input())
ans = [0] * 6
for _ in range(N):
    max_temp, min_temp = map(float, input().split())
    if max_temp >= 35:
        ans[0] += 1
    if 30 <= max_temp < 35:
        ans[1] += 1
    if 25 <= max_temp < 30:
        ans[2] += 1
    if min_temp >= 25:
        ans[3] += 1
    if min_temp < 0 and max_temp >= 0:
        ans[4] += 1
    if max_temp < 0:
        ans[5] += 1
print(*ans)
