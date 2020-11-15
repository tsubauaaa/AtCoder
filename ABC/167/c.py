def list_add(l1, l2):
    return [a + b for a, b in zip(l1, l2)]


N, M, X = map(int, input().split())
books = [list(map(int, input().split())) for i in range(N)]
ans = []
for i in range(2 ** N):
    p = [0 for _ in range(M + 1)]
    for j in range(N):
        if (i >> j) & 1 == 1:
            p = list_add(p, books[j])
    for k in range(1, M + 1):
        if p[k] < X:
            break
    else:
        ans.append(p[0])
print(min(ans) if len(ans) != 0 else -1)
