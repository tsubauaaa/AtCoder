import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.extend(B)
ans = []
for k, v in collections.Counter(A).items():
    if v > 1:
        ans.append(k)
ans.sort()
print(*ans)

