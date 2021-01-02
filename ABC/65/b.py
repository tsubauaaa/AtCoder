N = int(input())
A = [int(input()) for _ in range(N)]
ans = []
light = 0
for i in range(N):
    ans.append(A[light])
    light = A[light] - 1
print(ans.index(2) + 1 if ans.count(2) != 0 else -1)
