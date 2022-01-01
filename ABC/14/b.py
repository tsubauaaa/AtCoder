n, X = map(int, input().split())
a = list(map(int, input().split()))
bin = str(format(X, "0" + str(n) + "b"))
ans = 0
for i in range(n):
    if bin[i] == "1":
        ans += a[n - 1 - i]
print(ans)
