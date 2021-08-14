S, T = map(int, input().split())
U = max(S, T)
ans = 0
for a in range(S + 1):
    for b in range(S + 1):
        for c in range(S + 1):
            if a + b + c > S or a * b * c > T:
                break
            ans += 1

print(ans)
