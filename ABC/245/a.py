A, B, C, D = map(int, input().split())

if A < C:
    print("Takahashi")
    exit()
elif C < A:
    print("Aoki")
    exit()
else:
    if B <= D:
        print("Takahashi")
        exit()
    else:
        print("Aoki")
        exit()
