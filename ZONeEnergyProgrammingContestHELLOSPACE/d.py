from itertools import groupby

S = input()
splits = S.split("R")
T = ""
for i in range(len(splits) - 1):
    T += splits[i]
    T = T[::-1]
T += splits[-1]

print(T)
