import fractions

N = int(input())
i = 0
while 2 ** i < 10 ** 18 + 1:
    print(i)
    a = N
    b = 2 ** i
    print(a % b)
    print(float(fractions.Fraction(a) / fractions.Fraction(b)))
    i += 1
