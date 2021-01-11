N = int(input())
scores = [int(input()) for _ in range(N)]
sum_s = sum(scores)
scores.sort()
min_s = 101
for i in range(N):
    if scores[i] % 10 != 0:
        min_s = min(min_s, scores[i])
if sum_s % 10 == 0:
    if min_s != 101:
        print(sum_s - min_s)
    else:
        print(0)
else:
    print(sum_s)
