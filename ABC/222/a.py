N = input()
if len(N) == 4:
    print(N)
else:
    print("0" * (4-len(N)) + N)
