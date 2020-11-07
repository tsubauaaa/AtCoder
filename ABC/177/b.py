S = input()
T = input()
match = 0
for i in range(len(S) - len(T) + 1):
    tmp = 0
    for j in range(len(T)):
        if S[i + j] == T[j]:
            tmp += 1
    match = max(match, tmp)

print(len(T) - match)
