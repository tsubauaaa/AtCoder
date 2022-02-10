N = int(input())
ans = 10 ** 5
for i in range(1, N):
    left = sum(list(map(int, str(i))))
    right = sum(list(map(int, str(N - i))))
    ans = min(ans, left + right)

print(ans)
