import sys

A, B, C, K = map(int, input().split())

if abs(A - B) > 10 ** 18:
    print("Unfair")
    sys.exit()

is_positive = False

if A < B:
    if K % 2 == 0:
        is_positive = True
else:
    if K % 2 == 0:
        is_positive = True

if is_positive:
    print(A - B)
else:
    print(B - A)
