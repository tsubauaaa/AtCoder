N = int(input())
ans = {}
for _ in range(N):
    S = input()
    if S in ans:
        ans[S] += 1
    else:
        ans[S] = 1
print(sorted(ans.items(), key=lambda item: item[1])[-1][0])
