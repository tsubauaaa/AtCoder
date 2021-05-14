from sys import stdin

N = int(input())
S = list(input())
Q = int(input())
first = S[:N]
second = S[N:]

for i in range(Q):
    T, A, B = map(int, stdin.readline().split())
    if T == 1:
        if B <= N:
            first[A - 1], first[B - 1] = first[B - 1], first[A - 1]
        elif A <= N and B > N:
            first[A - 1], second[B - 1 - N] = second[B - 1 - N], first[A - 1]
        else:
            second[A - 1 - N], second[B - 1 - N] = second[B - 1 - N], second[A - 1 - N]
    else:
        first, second = second, first
print("".join(first + second))
