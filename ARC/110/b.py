N = int(input())
T = input()
S = "110" * 10 ** 4
cnt = 0
for i in range(len(S) - (N - 1)):
    if S[i : i + N] == T:
        cnt += 1
print(cnt)
print(9999999999 / cnt)
print(9999999993 / cnt)
