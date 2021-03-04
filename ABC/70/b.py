A, B, C, D = map(int, input().split())
if A < C < B < D:
    print(B - C)
elif A <= C < D <= B:
    print(D - C)
elif A < B < C < D:
    print(0)
elif C <= A < D <= B:
    print(D - A)
elif C <= A < B <= D:
    print(B - A)
elif C < D < A < B:
    print(0)
else:
    print(0)
