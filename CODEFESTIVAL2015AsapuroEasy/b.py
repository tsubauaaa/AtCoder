N = int(input())
S = input()
if N % 2 != 0:
    print(-1)
    exit()
S1 = S[: N // 2]
S2 = S[N // 2 :]
ans = 0
for s1, s2 in zip(S1, S2):
    if s1 != s2:
        ans += 1
print(ans)
