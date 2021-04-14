from collections import Counter


def count_diff(X, Y):
    cnt = 0
    for x, y in zip(X, Y):
        if x != y:
            cnt += 1
    return cnt


N = int(input())
A = input()
B = input()
C = input()

T = ""
for a, b, c in zip(A, B, C):
    cnt = 0
    max_dup = ""
    for k, v in Counter([a, b, c]).items():
        if v > cnt:
            cnt = v
            max_dup = k
    T += max_dup

print(count_diff(A, T) + count_diff(B, T) + count_diff(C, T))
