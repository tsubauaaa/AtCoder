S = list(input())
K = int(input())
T = S * 2
cnt = 0
for i in range(len(T) - 1):
    if T[i] == T[i + 1]:
        cnt += 1
        T[i + 1] = "0"
print(T)
if S[0] == S[-1]:
    if T[-1] != "0":
        d = 1
print(int(cnt / 2 * K))
