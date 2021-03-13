A, B, W = map(int, input().split())
W = W * 1000
ans = []
for i in range(1, W + 1):
    if A <= W / i <= B:
        ans.append(i)
print(f"{ans[0]} {ans[-1]}" if len(ans) != 0 else "UNSATISFIABLE")
