import copy
import itertools

cards=list(map(int,input().split()))
K=int(input())

selects = [i for i in range(3)]

c = itertools.combinations_with_replacement(selects,K)

for ci in c:
    casted = copy.deepcopy(cards)
    for cij in ci:
        casted[cij] *= 2
    if casted[1] > casted[0] and casted[2] > casted[1]:
        print("Yes")
        exit()
print("No")
