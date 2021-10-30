import itertools
S = list(input())

print(len(set(itertools.permutations(S,3))))