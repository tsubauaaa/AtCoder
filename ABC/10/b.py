n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
res = []
for i in range(1, max_a + 1):
    p1 = "d" if i % 2 == 0 else "l"
    p2 = "d" if (i + 1) % 3 == 0 else "l"
    res.append([i, p1, p2])
after = [0] * n
for i in range(n):
    for j in range(1, a[i] + 1):
        if res[j - 1][1] == res[j - 1][2] == "l":
            after[i] = res[j - 1][0]
ans = 0
for b, a in zip(a, after):
    ans += b - a
print(ans)
