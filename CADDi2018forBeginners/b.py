N, H, W = map(int, input().split())
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    if H <= A and W <= B:
        ans += 1

print(ans)
