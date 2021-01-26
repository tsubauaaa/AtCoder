N, va, vb, L = map(int, input().split())
ans = 0
for i in range(N):
    L = L / va * vb
print(L)
