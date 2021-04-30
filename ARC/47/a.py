N, L = map(int, input().split())
S = input()
tabs = 1
ans = 0
for i in range(N):
    if tabs > L:
        ans += 1
        tabs = 1
    if S[i] == "+":
        tabs += 1
    else:
        tabs -= 1

print(ans + 1 if tabs > L else ans)
