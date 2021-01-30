X, K, D = map(int, input().split())
remain = K - X // D
if remain > 0:
    if remain % 2 == 0:
        print(abs(X - remain * D))
    else:
        print(X - remain * D)
        print(abs(X - remain * D - D))
else:
    print(X - K * D)
