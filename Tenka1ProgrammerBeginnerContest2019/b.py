N = int(input())
S = input()
K = int(input())
T = S[K - 1]
ans = ""
for s in S:
    if s != T:
        ans += "*"
    else:
        ans += s
print(ans)
