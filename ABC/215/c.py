import itertools

S, K = input().split()
S = sorted(S)
K = int(K)
perms = set(itertools.permutations(S, len(S)))

P = []
for p in perms:
    P.append(''.join(p))
P.sort()
print(P[K - 1])
