Y = int(input())

if Y == 2000:
    print(2002)
    exit()

ans = []

for i in range(2000, 3003):
    if i % 4 == 2:
        ans.append(i)

for i in range(len(ans) - 1):
    if ans[i] < Y <= ans[i + 1]:
        print(ans[i + 1])

