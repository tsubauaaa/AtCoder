H, W = map(int, input().split())
h = 0
w = 0
for i in range(H):
    S = list(input().split())
    for j in range(W):
        if S[j] == "snuke":
            h = i
            w = j
alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
print(alphabets[w] + str(h + 1))
