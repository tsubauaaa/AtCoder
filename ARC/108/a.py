import itertools


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table


S, P = map(int, input().split())

divisors = divisor(P)
for c in itertools.combinations_with_replacement(divisors, 2):
    if sum(c) == S:
        print("Yes")
        exit()
print("No")
