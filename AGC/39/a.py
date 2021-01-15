from itertools import groupby

S = input()  # issii
for c, g in groupby(S):
    print(c, len(list(g)))
    # i 1
    # s 2
    # i 2
