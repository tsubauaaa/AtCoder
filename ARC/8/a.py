N = input()
if len(N) > 1:
    n1 = int(N[1])
    n2 = int(N[0])
else:
    n1 = int(N)
    n2 = 0

if n1 * 15 < 100:
    print(n1 * 15 + n2 * 100)
else:
    print(100 + n2 * 100)
