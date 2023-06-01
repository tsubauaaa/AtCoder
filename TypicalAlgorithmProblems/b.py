N = int(input())
BA = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    BA.append([b, a])

BA.sort()

last = 0
ans = 0

for b, a in BA:
    if last > a:
        continue
    ans += 1
    last = b

print(ans)
