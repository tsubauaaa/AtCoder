N = int(input())
ans = 10 ** 9 + 1
for i in range(N):
    A, P, X = map(int, input().split())
    remain = X - A
    if remain > 0:
        ans = min(ans, P)
print(ans if ans != 10 ** 9 + 1 else -1)
