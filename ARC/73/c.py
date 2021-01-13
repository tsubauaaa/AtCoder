N, T = map(int, input().split())
t = list(map(int, input().split()))
X = 0
for i in range(1, N):
    if t[i] - t[i - 1] <= T:
        d = t[i] - t[i - 1]
    else:
        d = T
    X += d
print(X + T)
