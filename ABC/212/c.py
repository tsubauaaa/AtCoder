import bisect

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 2*10**9+1

for a in A:
    i = bisect.bisect_left(B, a)
    if i != 0:
        tmp = abs(a - B[i-1])
    else:
        tmp = abs(a - B[i])

    if i != M:
        tmp2 = abs(a - B[i])
    else:
        tmp2 = abs(a - B[i-1])

    ans = min(ans, tmp)
    ans = min(ans, tmp2)

print(ans)
