N, S, D = map(int, input().split())
ans = False
for i in range(N):
    X, Y = map(int, input().split())
    if X >= S or Y <= D:
        continue
    else:
        ans = True
print("Yes" if ans else "No")
