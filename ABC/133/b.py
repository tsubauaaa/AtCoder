import math

N, D = map(int, input().split())
X = []
ans = 0

for i in range(N):
    X.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        tmp = 0
        for k in range(D):
            tmp += abs(X[i][k] - X[j][k]) ** 2

        if math.sqrt(tmp).is_integer():
            ans += 1

print(ans)
