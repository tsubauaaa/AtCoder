from collections import Counter


def score(cntr):
    score = 0
    for i in range(1, 10):
        score += i * 10 ** cntr[f"{i}"]
        print(score)
    return score


K = int(input())
S = input()
T = input()
print(Counter(S))
score = score(Counter(S))
print(score)
