from itertools import groupby

import numpy as np

N = int(input())
x_cnt = 0
matrix = []
for i in range(N):
    xn = input()
    x_cnt += xn.count("x")
    matrix.append(list(xn))
o_matrix = np.array(matrix).T.tolist()
o_cnt = 0
for om in o_matrix:
    for c, g in groupby(om):
        if c == "o":
            o_cnt += 1
print(x_cnt + o_cnt)
