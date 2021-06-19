N = int(input())
A = list(map(int, input().split()))

A1 = A[:N // 2]
if N % 2 == 0:
    A2 = A[N // 2:]
else:
    A2 = A[N // 2 + 1:]
A2 = A2[::-1]
d = {}
ans1 = 0
for a1, a2 in zip(A1, A2):
    if a1 in d:
        a1 = d[a1]
    if a2 in d:
        a2 = d[a2]
    if a1 != a2:
        d[a2] = a1
        ans1 += 1

d = {}
ans2 = 0
for a2, a1 in zip(A2, A1):
    if a2 in d:
        a2 = d[a2]
    if a1 in d:
        a1 = d[a1]
    if a2 != a1:
        d[a1] = a2
        ans2 += 1

print(min(ans1, ans2))
