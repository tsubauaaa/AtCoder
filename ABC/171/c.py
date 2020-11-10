N = int(input())
q = N // 26
m = N % 26
alphas = [
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
n = 1
while True:
    target = 0
    for i in range(n):
        target += 26 ** i
    if target <= N < target + 26 ** n:
        print(f"n: {n}, q: {q}, m: {m}")
        ans = alphas[(q - 1)] * (n - 1) + alphas[m - 1]
        print(ans)
        break
    n += 1
