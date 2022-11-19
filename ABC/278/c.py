N, Q = map(int, input().split())
follows = {}
ans = []
for q in range(Q):
    T, A, B = map(int, input().split())
    if A not in follows:
        follows[A] = set()
    if B not in follows:
        follows[B] = set()
    if T == 1:
        follows[A].add(B)
    elif T == 2:
        follows[A].discard(B)
    else:
        if A in follows[B] and B in follows[A]:
            ans.append("Yes")
        else:
            ans.append("No")

for ai in ans:
    print(ai)