import copy

N = int(input())
p = list(map(int, input().split()))
desc_p = sorted(p)
if p == desc_p:
    print("YES")
    exit()
for i in range(N):
    for j in range(N):
        tmp = copy.deepcopy(p)
        if i == j:
            continue
        tmp[i], tmp[j] = p[j], p[i]
        if tmp == desc_p:
            print("YES")
            exit()
print("NO")
