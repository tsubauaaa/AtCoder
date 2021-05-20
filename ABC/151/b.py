N, K, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)

X = M * N - total

if X < 0:
    print(0)
elif X > K:
    print(-1)
else:
    print(X)
