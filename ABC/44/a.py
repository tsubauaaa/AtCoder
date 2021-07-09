N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N - K > 0:
    M = N - K
    print(K * X + M * Y)
else:
    print(N * X)
