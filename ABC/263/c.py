import itertools

N, M = map(int, input().split())

all_num_iter = itertools.combinations(range(1, M + 1), N)

for nums in all_num_iter:
    print(*nums)
