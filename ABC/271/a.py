N = int(input())
h = format(N, "x").upper()

if len(h) == 1:
    print("0" + h)
else:
    print(h)
