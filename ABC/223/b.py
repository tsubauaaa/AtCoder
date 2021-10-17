S = input()
len_S = len(S)
ans = []
for i in range(len_S):
    S = S[1:]+S[0]
    ans.append(S)

ans.sort()

print(ans[0])
print(ans[-1])