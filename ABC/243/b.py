N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = 0
ans2 = 0

for a, b in zip(A, B):
    if a == b:
        ans1 += 1

print(ans1)

A_set = set(A)
B_set = set(B)

C = list(A_set & B_set)

for c in C:
    if A.index(c) != B.index(c):
        ans2 += 1

print(ans2)
