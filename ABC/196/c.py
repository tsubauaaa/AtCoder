N = int(input())
digit = len(str(N))
ans = 0
if digit % 2 != 0:
    if 10 <= N <= 999:
        ans = 9
    elif 1000 <= N <= 99999:
        ans = 99
    elif 100000 <= N <= 9999999:
        ans = 999
    elif 10000000 <= N <= 999999999:
        ans = 9999
    elif 1000000000 <= N <= 99999999999:
        ans = 99999
    elif 1000000000 <= N <= 99999999999:
        ans = 999999
else:
    S = str(N)
    if int(S[: digit // 2]) - int(S[digit // 2 :]) <= 0:
        ans = S[: digit // 2]
    else:
        ans = int(S[: digit // 2]) - 1
print(ans)

# ans2 = 0
# for i in range(1, N + 1):
#     d = len(str(i))
#     if d % 2 != 0:
#         continue
#     s = str(i)
#     if s[: d // 2] == s[d // 2 :]:
#         ans2 += 1
# print(ans2)
