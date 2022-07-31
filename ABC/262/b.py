import copy

N, M = map(int, input().split())
g = {i + 1: [] for i in range(N)}

for i in range(M):
    U, V = map(int, input().split())
    g[U].append(V)
    g[V].append(U)

ans = []

for k, v in g.items():
    for b in v:
        cs = copy.deepcopy(v)
        cs.remove(b)
        for c in cs:
            if c in g[b]:
                ans.append(sorted([k, b, c]))


print(len(list(map(list, set(map(tuple, ans))))))
