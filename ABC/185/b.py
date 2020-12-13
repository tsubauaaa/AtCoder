import copy

N, M, T = map(int, input().split())
n = copy.deepcopy(N)
t = 0
for i in range(M):
    A, B = map(int, input().split())
    n -= (A - t) * 1
    t = B
    if n <= 0:
        print("No")
        exit()
    n += (B - A) * 1
    n = min(N, n)
n -= (T - t) * 1
print("Yes" if n > 0 else "No")
