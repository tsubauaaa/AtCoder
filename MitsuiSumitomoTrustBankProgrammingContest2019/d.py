import itertools

N = int(input())
S = list(input())
print(len(list(itertools.combinations(S, 3))))
