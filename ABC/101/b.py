N = input()


def S(N):
    Sn = 0
    for n in N:
        Sn += int(n)
    return Sn


Sn = S(N)
print("Yes" if int(N) % Sn == 0 else "No")
