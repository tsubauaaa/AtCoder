X, A, B = map(int, input().split())
if B > A:
    if B - A > X:
        print("dangerous")
    else:
        print("safe")
else:
    print("delicious")
