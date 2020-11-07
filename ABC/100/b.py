D, N = map(int, input().split())
if N == 100:
    if D == 0:
        ans = 101
    elif D == 1:
        ans = 10100
    else:
        ans = 1010000
else:
    ans = 100 ** D * N

print(ans)
