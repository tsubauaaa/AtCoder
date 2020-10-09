N, K, Q = map(int, input().split())
ans = [K for _ in range(N)]


for i in range(Q):
    A = int(input())
    ans[A - 1] += 1

ans = list(map(lambda x: x - Q, ans))

for j in ans:
    if j <= 0:
        print("No")
    else:
        print("Yes")
