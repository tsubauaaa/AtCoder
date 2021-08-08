import copy
N = int(input())
A = list(map(int, input().split()))
B = sorted(copy.deepcopy(A))

b = B[-2]

print(A.index(b) + 1)
