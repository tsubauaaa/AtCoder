import copy

S = input()

rows = [[7], [4], [2, 8], [1, 5], [3, 9], [6], [10]]
memo = {1: 3, 2: 2, 3: 4, 4: 1, 5: 3, 6: 5, 7: 0, 8: 2, 9: 4, 10: 6}

if S[0] != "0":
    print("No")
    exit()

for i in range(10):
    if S[i] == "0":
        row = memo[i + 1]
        rows[row].remove(i + 1)

empty_cnt = 0
for i in range(7):
    if len(rows[i]) == 0:
        empty_cnt += 1
    else:
        empty_cnt = 0

    if empty_cnt >= 2:
        rows[i].append(0)

new_rows = []
for i in range(7):
    if len(rows[i]) == 0:
        new_rows.append(rows[i])
        continue
    if rows[i][0] == 0:
        continue

    new_rows.append(rows[i])

for i in range(len(new_rows) - 1):
    if i == 0:
        continue
    if len(new_rows[i]) == 0:
        if len(new_rows[i - 1]) > 0 and len(new_rows[i + 1]) > 0:
            print("Yes")
            exit()

print("No")
