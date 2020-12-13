S = input()

for i in range(len(S) - 1, -1, -1):
    len_s = len(S[0:i])
    if len_s % 2 != 0:
        continue
    if S[0 : len_s // 2] == S[len_s // 2 : i]:
        print(len(S[0:i]))
        exit()
