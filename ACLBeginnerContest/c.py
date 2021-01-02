def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 
    parents[x] = y


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())
    unite(A, B)

print(parents)
