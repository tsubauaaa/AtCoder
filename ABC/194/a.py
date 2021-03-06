A, B = map(int, input().split())

if B >= 8 and A + B >= 15:
    print(1)
elif A + B >= 10 and B >= 3:
    print(2)
elif A + B >= 3:
    print(3)
else:
    print(4)
