import math

N = int(input())

alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

i = 1
ans = 0
while ans < N:
    ans += 26 ** i
    i += 1

for j in range(i - 1):
    print(N, alphabets[int(N) % 26 - 1], int(N) % 26)
    N /= 26
    N -= N % 26
