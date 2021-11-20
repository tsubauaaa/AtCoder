N, X = map(int, input().split())
A = list(map(int, input().split()))

knows = [False] * N
knows[X-1] = True
for i in range(N):
    if knows[A[X-1]-1]:
        break
    knows[A[X-1]-1] = True
    X = A[X-1]
print(sum(knows))
