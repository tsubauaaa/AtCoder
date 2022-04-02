import collections

X = []
Y = []
for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = []
for k, v in collections.Counter(X).items():
    if v == 1:
        ans.append(k)

for k, v in collections.Counter(Y).items():
    if v == 1:
        ans.append(k)

print(*ans)
