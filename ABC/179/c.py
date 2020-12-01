N = int(input())
ans = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if N - a * b > 0:
            ans += 1
        else:
            break
print(ans)
