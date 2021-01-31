X, K, D = map(int, input().split())
X = abs(X)
q = X // D
remain = K - q
r = X % D
if remain < 0:
    print(X - K * D)
else:
    if remain % 2 == 0:
        print(r)
    else:
        print(abs(r - D))
