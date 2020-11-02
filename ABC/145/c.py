import math

N = int(input())
X = []
Y = []
ans = 0
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        ans += math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
        cnt += 1

print(ans * math.factorial(N) * (N - 1) / cnt / math.factorial(N))
