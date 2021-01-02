from collections import Counter

N = int(input())
S = []
e_S = []
for i in range(N):
    s = input()
    if s[0] == "!":
        e_S.append(s[1:])
    else:
        S.append(s)
S = list(set(S))
e_S = list(set(e_S))
S.extend(e_S)

for k, v in Counter(S).items():
    if v > 1:
        print(k)
        exit()
print("satisfiable")
