S = input()
seps = list(map(int, input().split()))
ans = ""
for i in range(len(S) + 1):
    if i in seps:
        ans += ans.join('"')
    if i == len(S):
        break
    ans += ans.join(S[i])
print(ans)
