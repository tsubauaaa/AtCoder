import sys
sys.setrecursionlimit(10**7)

path = {i: [] for i in range(4)}
for _ in range(3):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)

print(path)


def dfs(x, check):
    print(check)
    if sum(check) == 4:
        print("YES")
        exit()
    for n in path[x]:
        if not check[n]:
            check[n] = True
            dfs(n, check)


# for i in range(4):
#     print(i)
#     check = [False] * 4
#     check[i] = True
#     dfs(i, check)

check = [False] * 4
dfs(2, check)
print("NO")
