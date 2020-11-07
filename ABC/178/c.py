from itertools import combinations_with_replacement

N = int(input())

tmp = [i for i in range(10)]
print(list(combinations_with_replacement(tmp, N - 2)))
