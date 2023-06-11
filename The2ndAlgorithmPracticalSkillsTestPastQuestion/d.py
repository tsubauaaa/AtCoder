def is_match(T, S):
    for i in range(len(S)-len(T)+1):
        ok = True
        for j in range(len(T)):
            if S[i+j] != T[j] and T[j] != ".":
                ok = False
        if ok:
            return True

    return False


S = input()
ans = []
C = "abcdefghijklmnopqrstuvwxyz."

for T in C:
    if is_match(T, S):
        ans.append(T)

for T in C:
    for T2 in C:
        if is_match(T+T2, S):
            ans.append(T+T2)

for T in C:
    for T2 in C:
        for T3 in C:
            if is_match(T+T2+T3, S):
                ans.append(T+T2+T3)

print(len(ans))
