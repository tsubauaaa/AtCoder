N = int(input())
S = input()
T = []
for i in range(N):
    if S[i] in T:
        T.remove(S[i])
    T.append(S[i])

print("".join(T))
