T = input()
S = [i for i in input()]


def swap(i, s):
    s[i], s[i + 1] = s[i + 1], s[i]
    return s


for i in range(len(S) - 1):
    S[i], S[i + 1] = S[i + 1], S[i]
    print(S)
    S[i + 1], S[i] = S[i], S[i + 1]
