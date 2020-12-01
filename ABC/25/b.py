N, A, B = map(int, input().split())
ans = 0
for i in range(N):
    d, m = map(str, input().split())
    if int(m) <= A:
        m = A
    elif int(m) >= B:
        m = B
    else:
        m = int(m)
    if d == "East":
        ans += m
    else:
        ans -= m
if ans > 0:
    print(f"East {ans}")
elif ans < 0:
    print(f"West {abs(ans)}")
else:
    print(ans)
