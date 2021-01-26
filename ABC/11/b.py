S = input()
S = S.lower()
ans = S[0].upper()
for i in range(1, len(S[1:]) + 1):
    ans += ans.join(S[i])
print(ans)
