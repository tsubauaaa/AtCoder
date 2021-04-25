from collections import deque
from sys import stdin

N = int(input())
S = input()
Q = int(input())
for i in range(Q):
    T, A, B = map(int, stdin.readline().split())
    if T == 1:
        S = "".join([S[: A - 1], S[B - 1], S[A : B - 1], S[A - 1], S[B:]])
    else:
        items = deque(list(S))
        items.rotate(N * -1)
        S = "".join(list(items))
print(S)
