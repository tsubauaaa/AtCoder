X, K, D = map(int, input().split())
remain = K - X // D
if remain % 2 == 0:
    print(abs(X - remain * D))
else:
    print(abs(X - (remain + 1) * D))
