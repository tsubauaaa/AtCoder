A, B = map(int, input().split())

test = {1: [1, 3, 5, 7], 2: [2, 6, 3, 7], 3: [4, 6, 5, 7]}

ans1 = [False, False, False]
ans2 = [False, False, False]

for k, v in test.items():
    if A in v:
        ans1[k - 1] = True
    if B in v:
        ans2[k - 1] = True
scores = [1, 2, 4]
ans = 0
i = 0
for a, b in zip(ans1, ans2):
    if a or b:
        ans += scores[i]
    i += 1
print(ans)
