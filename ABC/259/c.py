from itertools import groupby

S = input()
T = input()

S_length = []
T_length = []

for c, g in groupby(S):
    S_length.append([c, len(list(g))])

for c, g in groupby(T):
    T_length.append([c, len(list(g))])

if len(S_length) != len(T_length):
    print("No")
    exit()

for s, t in zip(S_length, T_length):
    if s[0] != t[0]:
        print("No")
        exit()
    if s[1] == 1:
        if t[1] != 1:
            print("No")
            exit()
    else:
        if s[1] > t[1]:
            print("No")
            exit()

print("Yes")
