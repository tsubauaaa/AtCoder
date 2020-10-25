N, M = map(int, input().split())
submit = [input().split() for _ in range(M)]
ac = [0] * N
wa = [0] * N
for i in range(M):
    result = submit[i][1]
    question_num = int(submit[i][0]) - 1
    if result == "AC" and ac[question_num] == 0:
        ac[question_num] = 1
    elif result == "WA" and ac[question_num] == 0:
        wa[question_num] += 1
for i in range(N):
    if ac[i] != 1:
        wa[i] = 0
print(sum(ac), sum(wa))
