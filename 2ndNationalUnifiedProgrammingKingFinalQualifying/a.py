N = int(input())

if N == 1:
    print(0)
    exit()

ans = 0
for i in range(1, N):
    if i == N - 1:
        continue
    ans += 1

print(ans // 2 if N % 2 == 0 else ans // 2 + 1)
