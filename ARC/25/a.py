D = list(map(int, input().split()))
J = list(map(int, input().split()))
ans = 0
for d, j in zip(D, J):
    if d > j:
        ans += d
    else:
        ans += j
print(ans)
