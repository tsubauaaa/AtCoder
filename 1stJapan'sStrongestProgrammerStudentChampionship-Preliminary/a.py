M, D = map(int, input().split())

ans = 0
for m in range(1, M + 1):
    for d in range(1, D + 1):
        d1 = d if len(str(d)) == 1 else int(str(d)[0])
        d2 = d % 10 if len(str(d)) > 1 else 1
        if m == d1 * d2 and d1 >= 2 and d2 >= 2:
            ans += 1

print(ans)
