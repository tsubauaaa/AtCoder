import copy

S = list(input())
N = len(S) - len("keyence") + 1

for i in range(N):
    for j in range(len(S) - i):
        T = copy.deepcopy(S)
        del T[j : j + i]
        if "".join(T) == "keyence":
            print("YES")
            exit()
print("NO")
