N = int(input())
X = list(map(int, input().split()))


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return min(a)


primes = set()
for x in X:
    primes.add(prime_factorize(x))

ans = 1
for p in primes:
    ans *= p
print(ans)
