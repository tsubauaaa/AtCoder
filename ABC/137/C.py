import collections

N = int(input())
S = ["".join(sorted(input())) for _ in range(N)]
c = collections.Counter(S)
print(c)
