import copy

A, B, C, D, E, F, X = map(int, input().split())

Y = copy.deepcopy(X)

takahashi = 0
while True:
    if X < A:
        break
    X -= A
    takahashi += A * B
    X -= C

takahashi += max(0, X) * B

aoki = 0
while True:
    if Y < D:
        break
    Y -= D
    aoki += D * E
    Y -= F

aoki += max(0, Y) * E

# print(takahashi, aoki, X, Y)

if takahashi > aoki:
    print("Takahashi")
elif aoki > takahashi:
    print("Aoki")
else:
    print("Draw")
