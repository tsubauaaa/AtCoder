L, H = map(int, input().split())
N = int(input())
for i in range(N):
    ans = 0
    A = int(input())
    if L <= A <= H:
        ans = 0
    elif A < L:
        ans = L - A
    elif H < A:
        ans = -1
    else:
        continue
    print(ans)
