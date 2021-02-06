V, T, S, D = map(int, input().split())
t = D / V
if T <= t <= S:
    print("No")
else:
    print("Yes")
