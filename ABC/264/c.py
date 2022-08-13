import copy
import itertools

H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

combs1 = list(itertools.combinations([i + 1 for i in range(H1)], H1 - H2))
combs2 = list(itertools.combinations([i + 1 for i in range(W1)], W1 - W2))

for i in range(len(combs1)):
    T = copy.deepcopy(A)
    for c, comb in enumerate(combs1[i]):
        del T[comb - 1 - c]
    for j in range(len(combs2)):
        TT = copy.deepcopy(T)
        # print(combs1[i], combs2[j], TT)
        for c, comb in enumerate(combs2[j]):
            for row in TT:
                if not 0 <= comb - 1 - c < len(row):
                    break
                del row[comb - 1 - c]
        if TT == B:
            print("Yes")
            exit()


print("No")

