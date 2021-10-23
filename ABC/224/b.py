import itertools

H,W=map(int,input().split())

i_list = [i for i in range(1, H+1)]
j_list = [i for i in range(1, W+1)]

A = []

for h in range(H):
    Aij = list(map(int, input().split()))
    A.append(Aij)

i_combs = set(itertools.combinations(i_list, 2))
j_combs = set(itertools.combinations(j_list, 2))

for i_comb in i_combs:
    for j_comb in j_combs:
        if i_comb[0] <= i_comb[1] and j_comb[0] <= j_comb[1]:
            if A[i_comb[0]-1][j_comb[0]-1] + A[i_comb[1]-1][j_comb[1]-1] > A[i_comb[1]-1][j_comb[0]-1] + A[i_comb[0]-1][j_comb[1]-1]:
                print("No")
                exit()

print("Yes")


