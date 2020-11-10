def remove_str_start_end(s, start, end, add):
    return int(s[:start] + s[end + 1 + add :])


N = input()
ans = []

# print(remove_str_start_end(N, 1, 1, 1))
# exit()
if int(N) % 3 == 0:
    print(0)
    exit()

for i in range(len(N)):
    for j in range(len(N) - 1):
        target = remove_str_start_end(N, i, i, j)
        # print(target)
        if target % 3 == 0:
            # print(j + 1)
            ans.append(j + 1)

if len(ans) > 0:
    print(min(ans))
else:
    print(-1)
