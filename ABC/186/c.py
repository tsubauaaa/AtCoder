N = int(input())
ans = 0
for i in range(1, N + 1):
    if "7" in str(i) or "7" in oct(i):
        ans += 1
    elif "7" in str(i) and "7" in oct(i):
        ans += 1
print(N - ans)
